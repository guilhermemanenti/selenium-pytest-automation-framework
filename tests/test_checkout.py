from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage

def test_complete_purchase_flow(driver):

    login_page = LoginPage(driver)
    inventory_page = InventoryPage(driver)
    cart_page = CartPage(driver)
    checkout_page = CheckoutPage(driver)

    login_page.open()
    login_page.login("standard_user", "secret_sauce")
    login_page.wait_for_inventory_page()

    inventory_page.add_product_to_cart()
    inventory_page.go_to_cart()

    cart_page.click_checkout()

    checkout_page.fill_information("Guilherme", "Manenti", "30123-000")
    checkout_page.continue_checkout()
    checkout_page.finish_checkout()

    message = checkout_page.get_complete_message()

    assert "Thank you for your order!" in message

    #simula erro e realiza o print de tela
    #assert "Mensagem Errada" in message
