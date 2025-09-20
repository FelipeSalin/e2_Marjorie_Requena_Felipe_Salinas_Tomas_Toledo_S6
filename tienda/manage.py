#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys
import oracledb
from dotenv import load_dotenv
load_dotenv()

lib_dir = os.environ.get("ORACLE_LIB_DIR")
tns_dir = os.environ.get("TNS_ADMIN_DIR")

if lib_dir and tns_dir:
    oracledb.init_oracle_client(lib_dir=lib_dir)
    os.environ["TNS_ADMIN"] = tns_dir



def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'tienda.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()
