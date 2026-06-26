from supabase import create_client

SUPABASE_URL = "https://ujshkntymusltjbcidip.supabase.co/rest/v1/"
SUPABASE_KEY = "sb_publishable_E6XZrGkPkmoRcJquExcR9Q_S1Ihrm3G"

supabase = create_client(SUPABASE_URL, SUPABASE_KEY)