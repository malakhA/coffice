:banner: banners/email_gateway.jpg

==================
COffice email gateway
==================

The COffice mail gateway allows you to inject directly all the received emails in COffice.

Its principle is straightforward: your SMTP server executes the "mailgate" script for every new incoming email.

The script takes care of connecting to your COffice database through XML-RPC, and send the emails via the MailThread.message_process() feature.

Prerequisites
-------------
- Administrator access to the COffice database.
- Your own mail server such as Postfix or Exim.
- Technical knowledge on how to configure an email server.

For Postfix
-----------
In you alias config (/etc/aliases):

.. code-block:: text

	email@address: "|/coffice-directory/addons/mail/static/scripts/coffice-mailgate.py -d <database-name> -u <userid> -p <password>"

.. note:: Resources
    - `Postfix <http://www.postfix.org/documentation.html>`
    - `Postfix aliases <http://www.postfix.org/aliases.5.html>`
    - `Postfix virtual <http://www.postfix.org/virtual.8.html>`


For Exim
--------
.. code-block:: text

	*: |/coffice-directory/addons/mail/static/scripts/coffice-mailgate.py -d <database-name> -u <userid> -p <password>

.. note:: Resources
    - `Exim <https://www.exim.org/docs.html>`


.. note:: If you don't have access/manage your email server, use `inbound messages<https://www.coffice.com/documentation/user/13.0/discuss/email_servers.html#how-to-manage-inbound-messages>`.
