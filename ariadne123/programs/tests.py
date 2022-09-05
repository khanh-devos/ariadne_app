
from django.test import TestCase, Client
from programs.models import Book

class GraphQLTest(TestCase):
    def test_list_books(self):
        Book.objects.create(title="Book Title")
        query = """
            query {
                books {
                    title
                }
            }
        """
        response = Client().post(
            "/graphql/",
            {"query": query},
            content_type="application/json"
        )
        
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json().get("errors"), None)
        
        books = response.json()["data"]["books"]
        self.assertEqual(len(books), 1)
        self.assertEqual(books[0]["title"], "Book Title")

    def test_create_book(self):
        mutation = """
            mutation create_book($title: String!, $published_at: Date!) {
                create_book(title: $title, published_at: $published_at) {
                    title
                }
            }
        """
        response = Client().post(
            "/graphql/",
            {"query": mutation, "variables": {
                "title": "Test createBook",
                "published_at": "2022-9-4"
                
            }},
            content_type="application/json"
        )
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json().get("errors"), None)
        self.assertEqual(response.json()["data"]["create_book"]["title"], "Test createBook")
