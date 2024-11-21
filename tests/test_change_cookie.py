def test_change_cookie(page):

    page.goto("https://www.ing.pl/")
    page.locator("button", has_text="Dostosuj").click()
    page.locator("label.cookie-policy-switch-label input#CpmAnalyticalOption").click()

    element = page.locator("label.cookie-policy-switch-label input#CpmAnalyticalOption")
    name_value = element.get_attribute("name")
    expected_name = "CpmAnalyticalOption"

    assert name_value == expected_name, f"Błąd! Oczekiwana wartość: {expected_name}, a znaleziono: {name_value}"
    print("Poprawnie wybrałeś Cookies analityczne!")

    page.get_by_role("button", name="Zaakceptuj wybrane").click()

    assert page.inner_text(
        "text=Twoje ustawienia zostały zapisane") == "Twoje ustawienia zostały zapisane", f"Actuall value: {page.inner_text('text = Twoje ustawienia zostały zapisane')}"

    banner_selector = "span"
    banner = page.locator(banner_selector).filter(has_text="Twoje ustawienia zostały zapisane")

    assert banner.is_visible(), "Baner z komunikatem 'Twoje ustawienia zostały zapisane' nie jest widoczny!"
    print("Baner 'Twoje ustawienia zostały zapisane' jest widoczny.")

    banner.wait_for(state="hidden", timeout=6000)       #czas ustawiony tak, aby test działał dla trzech przegądarek
    assert banner.is_hidden(), "Baner nie zniknął po czasie oczekiwania!"
    print("Baner zniknął poprawnie po kilku sekundach.")