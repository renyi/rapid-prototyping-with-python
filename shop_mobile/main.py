from kivy.app import App
from kivy.uix.listview import ListView
from kivy.uix.gridlayout import GridLayout
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.widget import Widget
from kivy.network.urlrequest import UrlRequest

from kivy.uix.image import Image, AsyncImage
from kivy.uix.label import Label
from kivy.uix.button import Button


class ShopHeader(GridLayout):
    """
    App Header
    """
    def __init__(self, **kwargs):
        kwargs['cols'] = 1 # Sets grid column to 1
        super(ShopHeader, self).__init__(**kwargs)
        label = Label(text="My Shop", valign="top")
        self.add_widget(label)


class ShopFooter(GridLayout):
    """
    App Footer
    """
    def __init__(self, **kwargs):
        kwargs['cols'] = 1 # Sets grid column to 1
        super(ShopFooter, self).__init__(**kwargs)
        label = Label(text="Rapid Prototyping with Python by Renyi Khor", valign="bottom")
        self.add_widget(label)


class ShopContent(GridLayout):
    """
    App Content
    """
    def __init__(self, **kwargs):
        kwargs['cols'] = 5 # Sets grid column to 5
        super(ShopContent, self).__init__(**kwargs)

        def on_success(req, result, *args):
            """
            API Callback
            """
            product_list = result

            # from pprint import pprint
            # pprint(result)

            for product in product_list:
                # print product['id']
                # print product['name']
                # print product['description']
                # print product['image']
                # print "*"*50

                """
                UI Stuffs
                """
                label = Label(text="%s" % product['id'], size_hint_x=None, width=50)
                self.add_widget(label)

                label2 = Label(text=product['name'], size_hint_x=None, width=200)
                self.add_widget(label2)

                label3 = Label(text=product['description'], shorten=True, text_size=(400, None))
                self.add_widget(label3)

                if product['image']:
                    image = AsyncImage(source=product['image'], allow_stretch=True, size_hint_x=None, width=80)
                    self.add_widget(image)
                else:
                    image = Image(source='img/default.jpg', size_hint_x=None, width=80)
                    self.add_widget(image)

                button = Button(text='Buy Now !', size_hint_x=None, width=100)
                self.add_widget(button)

        """
        API Call
        """
        url = 'http://localhost:8000/api/products/'
        headers = {
            'Content-Type': 'application/json',
        }
        UrlRequest(url, req_headers=headers, on_success=on_success)


class ShopApp(App):
    def build(self):
        """
        Main Layout of App
        """
        MainLayout = GridLayout(cols=1)
        MainLayout.add_widget(ShopHeader(size_hint_y=None, height=80))
        MainLayout.add_widget(ShopContent())
        MainLayout.add_widget(ShopFooter(size_hint_y=None, height=80))
        return MainLayout


if __name__ == '__main__':
    ShopApp().run()
