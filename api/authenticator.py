import os
from fastapi import Depends
from jwtdown_fastapi.authentication import Authenticator
from queries.accounts import AccountQueries
from models.accounts import AccountOut, AccountOutWithHashedPassword


class MindscribeAuthenticator(Authenticator):
    async def get_account_data(
        self,
        username: str,
        accounts: AccountQueries,
    ):
        # Use your repo to get the account based on the
        # username (which could be an email)
        return accounts.get(username)

    def get_account_getter(
        self,
        accounts: AccountQueries = Depends(),
    ):
        # Return the accounts. That's it.
        return accounts

    def get_hashed_password(self, account):
        if isinstance(account, dict):
            return None

        if isinstance(account, AccountOutWithHashedPassword):
            return account.hashed_password
        return None

    def get_account_data_for_cookie(
        self, account: AccountOutWithHashedPassword
    ):
        # Return the username and the data for the cookie.
        # You must return TWO values from this method.
        return account.username, AccountOut(**account.dict())


authenticator = MindscribeAuthenticator(os.environ["SIGNING_KEY"])
