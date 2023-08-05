import flet as ft
from supabase import create_client, Client

URL = "https://miqibunydpqfzitmhwdp.supabase.co"
KEY = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6Im1pcWlidW55ZHBxZnppdG1od2RwIiwicm9sZSI6InNlcnZpY2Vfcm9sZSIsImlhdCI6MTY4ODE3NjA5NywiZXhwIjoyMDAzNzUyMDk3fQ.KS2Sd3M_1IQbDAeSwZehWgPQZ7coHmT3dvxOv6ifBY4"

def supa():
    return create_client(URL, KEY)

def main(page:ft.Page):
    page.title="python"
    supabase = supa()
    def button(e):
        print("안녕", filed.value)
        supabase.table("name_table").insert({"name":filed.value}).execute()
        name_rander()
        #n = ft.Text(filed.value)
        #col.controls.append(n)
        filed.value=""
        page.update()

    txt = ft.Text("이름이 무엇인가요??",size=20)
    filed =ft.TextField(hint_text="입력창")
    btn = ft.TextButton("눌러", on_click=button)
    row = ft.Row()
    col = ft.Column()
    supabase = supa()
    def name_rander():
        r = supabase.table("name_table").select("*").limit(1).execute()
        for i  in range(len(col.controls)):
            col.controls.pop()
            
        for info in r.data:
            t = ft.Text(info["name"]+"님 안녕하세요.")
            col.controls.append(t)
    name_rander()
    page.add(col)
    page.add(txt)
    page.add(filed)
    page.add(btn)
    page.update()

ft.app(target=main)
