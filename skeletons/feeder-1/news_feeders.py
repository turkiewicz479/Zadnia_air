#!/usr/bin/python
# -*- coding: utf-8 -*-

from typing import List


class News:
    """Nowinka.

    Atrybuty:
        title (str): tytuł nowinki
        pub_date (str): data nowinki w formacie "DD Mmm YYYY" (np. "01 Jan 2018")
            Próba ustawienia źle sformatowanej daty powinna skutkować błędem typu ValueError.
            Poprawna data składa się z ciągu:
                "<2x cyfra> <duża litera><2x mała litera> <4x cyfra>"

    Reprezentacja tekstowa:
        "[DD Mmm YYYY] <tytuł>"
    """
    # TODO: zaimplementuj...
    pass


# TODO: Zaimplementuj `NewsFeeder` jako klasę abstrakcyjną.
class NewsFeeder:
    """Klasa dostarczająca zestawienia nowinek ze strumienia RSS.

    Atrybuty:
        rss_url (str): URL strony zawierającej strumień RSS
    """

    def __init__(self, rss_url: str, *args, **kwargs) -> None:
        """
        Parametry:
         rss_url -- URL strony zawierającej strumień RSS
        """
        # TODO: Zaimplementuj jako metodę abstrakcyjną.
        raise NotImplementedError

    def get_feed(self) -> List[News]:
        """Zwróć listę artykułów ze strumienia RSS.
        """
        # TODO: Zaimplementuj jako metodę abstrakcyjną.
        raise NotImplementedError


class BBCNewsFeeder(NewsFeeder):
    # TODO: zaimplementuj...
    pass
