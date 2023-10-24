import os
from dotenv import load_dotenv
from supabase import create_client, Client


os.environ["SUPABASE_URL"] = "https://bkxlgoiyqsmvsykhgopu.supabase.co"
os.environ["SUPABASE_KEY"] = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImJreGxnb2l5cXNtdnN5a2hnb3B1Iiwicm9sZSI6ImFub24iLCJpYXQiOjE2OTQ2NTIyNzIsImV4cCI6MjAxMDIyODI3Mn0.N64l3Prio2ucUYXv65UBhq_wxa0lVk62_00nGvCeH38"


def add_entries(supabase, id, first_name,last_name,codename):
    value = {'id': id, 'first_name': first_name, 'last_name': last_name, 'codename': codename}
    data = supabase.table('player').insert(value).execute()

def remove_entries(supabase, id):
    data = supabase.table('player').delete().eq("id", id).execute()

def update_entries(supabase, newid, previd, first_name, last_name, codename):
    data = supabase.table('player').update({"id": newid, 'first_name': first_name, 'last_name': last_name, 'codename': codename}).eq("id", previd).execute()

def select_entries(supabase, id):
    data = supabase.table('player').select('*').execute()

def player_exists(supabase, id):
    query = supabase.table('player').select('id').eq('id', id)
    result = query.execute()
    return len(result.data) > 0



# def main():
#     vendor_count = 10
#     load_dotenv()
#     url: str = os.environ.get("SUPABASE_URL")
#     key: str = os.environ.get("SUPABASE_KEY")
#     supabase: Client = create_client(url, key)
#     add_entries(supabase, 57, "Jim", "Beam", "Whiskey")

# main()
