import os
import json
from dotenv import load_dotenv
from supabase import create_client, Client
from faker import Faker
import faker_commerce


def add_entries(supabase, id, first_name,last_name,codename):
    value = {'id': id, 'first_name': first_name, 'last_name': last_name, 'codename': codename}
    data = supabase.table('player').insert(value).execute()

def remove_entries(supabase, id):
    data = supabase.table('player').delete().eq("id", id).execute()

def update_entries(supabase, newid, previd, first_name, last_name, codename):
    data = supabase.table('player').update({"id": newid, 'first_name': first_name, 'last_name': last_name, 'codename': codename}).eq("id", previd).execute()



def main():
    vendor_count = 10
    load_dotenv()
    url: str = os.environ.get("SUPABASE_URL")
    key: str = os.environ.get("SUPABASE_KEY")
    supabase: Client = create_client(url, key)
    #add_entries(supabase, 45, 'Tyler', 'Dodson', 'Dotty')
    update_entries(supabase, 46, 45, 'Joe', 'Bergin', 'pomelo')

main()
