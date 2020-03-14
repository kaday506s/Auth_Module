import logging
from datetime import datetime
from ldap3 import Server, Connection, ALL, SUBTREE, ALL_ATTRIBUTES

# My libs
from apps.authorization.models import LdapSettings
from apps.contribe.logging_module import Logger


class LdapBackend:
    @staticmethod
    def get_ldap_user(username, password):
        logger = Logger._logging(LdapBackend.__name__)

        ldap_settings = LdapSettings.objects.all()

        for ldap_set in ldap_settings:
            try:
                server = Server(ldap_set.settings[0].get('LDAP_URL'),
                                get_info=ALL,
                                use_ssl=True,
                                allowed_referral_hosts=[('*', True)],
                                port=ldap_set.settings[0].get('PORT')
                                )
                connection = Connection(
                                server,
                                f'{ldap_set.settings[0].get("DOMAIN")}{username}',
                                password,
                                auto_bind=True
                                )
            except Exception as ex:
                logger.warning(f"\nLdap set ===> {str(ldap_set.settings)}"
                               f"\nDate ===> {datetime.now()}"
                               f"\nUSER ===> {username}"
                               f"\nException ==> {ex}\n")
                continue

            else:
                connection.search(
                    search_base=ldap_set.settings[0]['LDAP_SEARCH_BASE'],
                    search_filter=f'(&(objectClass=Person)(sAMAccountName={username}))',
                    search_scope=SUBTREE,
                    attributes=ALL_ATTRIBUTES,)

                logger.warning(f"\nLdap set ===> {str(ldap_set.settings)}"
                               f"\nDate ===> {datetime.now()}"
                               f"\nUSER ===> {username} "
                               f"\nStatus ==> OK!\n"
                               
                               f"\nSEARCHING... \n"
                               )

                if len(connection.response) >= 1:
                    logger.warning(f"RESULT ===> TRUE")
                    return connection.response[0]

                logger.warning(f"RESULT ===> FALSE")
        return False

