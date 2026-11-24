# Nefunkční odkazy na www.mlp.cz

Kontrola proběhla 22. 11. 2026. Prošli jsme **1 393 stránek** ze sitemapy a ověřili **10 624 adres** (odkazy i obrázky). Nalezeno **215 chybných odkazů na 320 stránkách**.

- Celý seznam jako tabulka pro Excel: [`report/opravy.xlsx`](report/opravy.xlsx) (jeden řádek = jedna stránka a jeden chybný odkaz, s filtry podle typu a priority).
- Jak kontrola proběhla: viz [konec stránky](#jak-kontrola-proběhla).

## Souhrn

| Typ chyby | Priorita | Počet |
|---|---|---:|
| [Chybně zapsaný odkaz](#malformed) | 1 | 41 |
| [Stará / neexistující adresa na mlp.cz](#old-url) | 1 | 34 |
| [Odkaz na starý / testovací web knihovny](#old-domain) | 1 | 12 |
| [Chybějící dokument / soubor](#document) | 1 | 11 |
| [Odkaz na nepublikovaný článek](#unpublished) | 1 | 9 |
| [Přepínač jazyka EN vede na 404](#lang-switch) | 1 | 1 |
| [Cizí web: stránka neexistuje (404)](#external-404) | 2 | 25 |
| [Nefunkční obrázek ze starého webu](#image) | 2 | 19 |
| [Neexistující záznam v katalogu](#catalog) | 2 | 1 |
| [Smazaná akce](#event) | 2 | 1 |
| [Cizí web nedostupný / zaniklý](#external-dead) | 3 | 42 |
| [Cizí web bez https – ověřit ručně](#external-http) | 3 | 17 |
| [Odkaz na prázdný výpis akcí](#listing-empty) | 3 | 2 |

Priorita 1 = odkaz vede na chybovou stránku nebo jde o chybu celého webu. Priorita 3 = ověřit ručně.

<a id="malformed"></a>

## Chybně zapsaný odkaz (41)

Priorita 1. Adresa je zapsaná chybně (přilepený text, chybějící doména, adresa interního serveru „//OREL/“, mezery). Stačí odkaz opravit v editoru – návrh správné adresy je v tabulce.

| Kde | Text odkazu | Chybný odkaz | Navržená oprava |
|---|---|---|---|
| [Tvůrčí psaní s Viktorem Špačkem II: obsazeno](https://www.mlp.cz/cz/akce/tvurci-psani-s-viktorem-spackem-ii-obsazeno/723)<br>[Tvůrčí psaní s Viktorem Špačkem: Petřiny: obsazeno](https://www.mlp.cz/cz/akce/tvurci-psani-s-viktorem-spackem-petriny-obsazeno/9819)<br>[Tvůrčí psaní s Ivanem A. Buninem: obsazeno](https://www.mlp.cz/cz/akce/tvurci-psani-s-ivanem-buninem-obsazeno/9839)<br>a dalších 26 | Viktorem Špačkem | `//OREL/katalog/osoba/spacek-viktor/1448672` | `https://www.mlp.cz/katalog/osoba/spacek-viktor/1448672` ✓ ověřeno |
| [Tvůrčí psaní s Viktorem Špačkem II: obsazeno](https://www.mlp.cz/cz/akce/tvurci-psani-s-viktorem-spackem-ii-obsazeno/723)<br>[Tvůrčí psaní s Viktorem Špačkem: Petřiny: obsazeno](https://www.mlp.cz/cz/akce/tvurci-psani-s-viktorem-spackem-petriny-obsazeno/9819)<br>[Tvůrčí psaní s Viktorem Špačkem I: obsazeno](https://www.mlp.cz/cz/akce/tvurci-psani-s-viktorem-spackem-i-obsazeno/703)<br>a dalších 19 | Ernesta Hemingwaye | `//OREL/katalog/osoba/hemingway-ernest/1169466` | `https://www.mlp.cz/katalog/osoba/hemingway-ernest/1169466` ✓ ověřeno |
| [Tvůrčí psaní s Viktorem Špačkem II: obsazeno](https://www.mlp.cz/cz/akce/tvurci-psani-s-viktorem-spackem-ii-obsazeno/723)<br>[Tvůrčí psaní s Viktorem Špačkem: Petřiny: obsazeno](https://www.mlp.cz/cz/akce/tvurci-psani-s-viktorem-spackem-petriny-obsazeno/9819)<br>[Tvůrčí psaní s Viktorem Špačkem I: obsazeno](https://www.mlp.cz/cz/akce/tvurci-psani-s-viktorem-spackem-i-obsazeno/703)<br>a dalších 19 | Raymonda Carvera | `//OREL/katalog/osoba/carver-raymond/1212424` | `https://www.mlp.cz/katalog/osoba/carver-raymond/1212424` ✓ ověřeno |
| [Tvůrčí psaní s Viktorem Špačkem II: obsazeno](https://www.mlp.cz/cz/akce/tvurci-psani-s-viktorem-spackem-ii-obsazeno/723)<br>[Tvůrčí psaní s Viktorem Špačkem: Petřiny: obsazeno](https://www.mlp.cz/cz/akce/tvurci-psani-s-viktorem-spackem-petriny-obsazeno/9819)<br>[Tvůrčí psaní s Viktorem Špačkem I: obsazeno](https://www.mlp.cz/cz/akce/tvurci-psani-s-viktorem-spackem-i-obsazeno/703)<br>a dalších 19 | Antona Pavloviče Čechova | `//OREL/katalog/osoba/cechov-anton-pavlovic/1177217` | `https://www.mlp.cz/katalog/osoba/cechov-anton-pavlovic/1177217` ✓ ověřeno |
| [Tvůrčí psaní s Ivanem A. Buninem: obsazeno](https://www.mlp.cz/cz/akce/tvurci-psani-s-ivanem-buninem-obsazeno/9839)<br>[Tvůrčí psaní s Ivanem A. Buninem: obsazeno](https://www.mlp.cz/cz/akce/tvurci-psani-s-ivanem-buninem-obsazeno/9841)<br>[Tvůrčí psaní s Ivanem A. Buninem: obsazeno](https://www.mlp.cz/cz/akce/tvurci-psani-s-ivanem-buninem-obsazeno/9843)<br>a dalších 4 | Ivana Alexejeviče Bunina | `//OREL/katalog/osoba/bunin-ivan-aleksejevic/1176558` | `https://www.mlp.cz/katalog/osoba/bunin-ivan-aleksejevic/1176558` ✓ ověřeno |
| [Jak používat knihovnu bez obsluhy?](https://www.mlp.cz/cz/novinky/jak-pouzivat-knihovnu-bez-obsluhy)<br>[Návod na knihovnu bez obsluhy](https://www.mlp.cz/cz/novinky/navod-na-knihovnu-bez-obsluhy)<br>[Knihovna bez obsluhy](https://www.mlp.cz/cz/napoveda/knihovna-bez-obsluhy) | Mého účtu | `https://napoveda/muj-ucet/` | `https://www.mlp.cz/napoveda/muj-ucet/` ✓ ověřeno |
| [Divadlo Říše loutek znovu otevřelo](https://www.mlp.cz/cz/novinky/divadlo-rise-loutek-znovu-otevrelo)<br>[Den dyslexie 2026](https://www.mlp.cz/cz/novinky/den-dyslexie-2026) | Ústřední knihovny / Ústřední knihovna | `//OREL/pobocky/ustredni-knihovna/` | `https://www.mlp.cz/pobocky/ustredni-knihovna/` ✓ ověřeno |
| [Staňte se praktikantem](https://www.mlp.cz/cz/kariera/stante-se-praktikantem) | personalni-vzdelavani@mlp.cz | `personalni-vzdelavani@mlp.cz` | `mailto:personalni-vzdelavani@mlp.cz` |
| [Samoobslužná pokladna](https://www.mlp.cz/cz/napoveda/bezhotovostni-placeni/samoobsluzna-pokladna) | Kiosek CČM | `https://pobocky/kiosek-ccm/` | `https://www.mlp.cz/pobocky/kiosek-ccm/` ✓ ověřeno |
| [Co si o knihovně myslí její návštěvníci?](https://www.mlp.cz/cz/novinky/co-si-o-knihovne-mysli-jeji-navstevnici) | Černý Most | `https://pobocky/cerny-most/` | `https://www.mlp.cz/pobocky/cerny-most/` ✓ ověřeno |
| [Co si o knihovně myslí její návštěvníci?](https://www.mlp.cz/cz/novinky/co-si-o-knihovne-mysli-jeji-navstevnici) | Rajská zahrada | `https://pobocky/rajska-zahrada` | `https://www.mlp.cz/pobocky/rajska-zahrada` ✓ ověřeno |
| [Čtete za nároďák?](https://www.mlp.cz/cz/novinky/ctete-za-narodak) | Verne | `https://www.mlp.cz/katalog/osoba/verne-jules/1190605,` | `https://www.mlp.cz/katalog/osoba/verne-jules/1190605` ✓ ověřeno |
| [Čtveráci z Břevnova – výstava fotografií Věry Pavly Dubské](https://www.mlp.cz/cz/novinky/ctveraci-z-brevnova-vystava-fotografii-very-pavly-dubske) | Břevnov | `//OREL/pobocky/brevnov/` | `https://www.mlp.cz/pobocky/brevnov/` ✓ ověřeno |
| [Divadelní a filmové oddělení uvádí: dokumentární filmy zada…](https://www.mlp.cz/cz/novinky/divadelni-filmove-oddeleni-uvadi-dokumentarni-filmy-zadarmo) | AFO | `https://afo.cz/` | `https://afo.cz/` |
| [Divadelní a filmové oddělení uvádí: dokumentární filmy zada…](https://www.mlp.cz/cz/novinky/divadelni-filmove-oddeleni-uvadi-dokumentarni-filmy-zadarmo) | Jaképak soužití, sakra! (KineDok) | `https://www.mlp.cz/cz/akce/kinedok-jakepak-souziti-sakra/10142` | `https://www.mlp.cz/cz/akce/kinedok-jakepak-souziti-sakra/10142` ✓ ověřeno |
| [Divadelní a filmové oddělení uvádí: dokumentární filmy zada…](https://www.mlp.cz/cz/novinky/divadelni-filmove-oddeleni-uvadi-dokumentarni-filmy-zadarmo) | V pasti kliknutím (AFO, dramaturgický úvod) | `https://www.mlp.cz/cz/akce/afo-v-pasti-kliknutim/9939` | `https://www.mlp.cz/cz/akce/afo-v-pasti-kliknutim/9939` ✓ ověřeno |
| [Divadlo, vzdělávání, popularizace — od září zase začínáme!](https://www.mlp.cz/cz/novinky/divadlo-vzdelavani-popularizace-od-zari-zase-zaciname) | Více informací zde >>> | `:%20https:/teatrologie.cz/aktuality/symposium-k-260-letum-existence-barokniho-divadla-v-ceskem-krumlove-progr…` | `https://teatrologie.cz/aktuality/symposium-k-260-letum-existence-barokniho-divadla-v-ceskem-krumlove-program/` |
| [Doučování angličtiny na Proseku](https://www.mlp.cz/cz/novinky/doucovani-anglictiny-na-proseku) | Prosek | `//OREL/pobocky/prosek/` | `https://www.mlp.cz/pobocky/prosek/` ✓ ověřeno |
| [Dvě výročí: Master of Puppets a David Gilmour](https://www.mlp.cz/cz/novinky/dve-vyroci-master-puppets-david-gilmour) | Pink Floyd- nahrávky a knihy k půjčení | `https://www.mlp.cz/katalog/osoba/pink-floyd-hudebni-skupina/1230664` | `https://www.mlp.cz/katalog/osoba/pink-floyd-hudebni-skupina/1230664` ✓ ověřeno |
| [Hudební novinky: září 2026](https://www.mlp.cz/cz/novinky/hudebni-novinky-zari-2026) | Hudební oddělení Ústřední knihovny | `//OREL/o-knihovne/sluzby/specializovana-oddeleni/hudebni-oddeleni` | `https://www.mlp.cz/o-knihovne/sluzby/specializovana-oddeleni/hudebni-oddeleni` ✓ ověřeno |
| [Jan Laichter – nakladatel, na kterého bychom neměli zapomen…](https://www.mlp.cz/cz/novinky/jan-laichter-nakladatel-na-ktereho-bychom-nemeli-zapomenout) | O umlčené kulturní epoše | `https://katalog/titul/o-umlcene-kulturni-epose/4627510` | `https://www.mlp.cz/katalog/titul/o-umlcene-kulturni-epose/4627510` ✓ ověřeno |
| [Jan Laichter – nakladatel, na kterého bychom neměli zapomen…](https://www.mlp.cz/cz/novinky/jan-laichter-nakladatel-na-ktereho-bychom-nemeli-zapomenout) | Myšlenky Boženy Němcové | `https://z/katalog/titul/myslenky-bozeny-nemcove/132523` | `https://www.mlp.cz/katalog/titul/myslenky-bozeny-nemcove/132523` ✓ ověřeno |
| [Jan Laichter – nakladatel, na kterého bychom neměli zapomen…](https://www.mlp.cz/cz/novinky/jan-laichter-nakladatel-na-ktereho-bychom-nemeli-zapomenout) | Nakladatel Jan Laichter | `https://z/katalog/titul/nakladatel-jan-laichter/2010581` | `https://www.mlp.cz/katalog/titul/nakladatel-jan-laichter/2010581` ✓ ověřeno |
| [Kamil Lhoták – obdivovatel dopravních prostředků](https://www.mlp.cz/cz/novinky/kamil-lhotak-obdivovatel-dopravnich-prostredku) | Hermann, Ignát: U snědeného krámu | `https://z/katalog/titul/4583196` | `https://www.mlp.cz/katalog/titul/4583196` ✓ ověřeno |
| [Knihovna na veletrzích i jako hostitel festivalů](https://www.mlp.cz/cz/novinky/knihovna-na-veletrzich-i-jako-hostitel-festivalu) | Projekce v Ústřední knihovně | `/akce/vsechny-akce?field_event_type_target_id=11&nid_entityreference_filter=571&field_event_instance_time_ran…` | `https://www.mlp.cz/akce/vsechny-akce?field_event_type_target_id=11&nid_entityreference_filter=571&field_event…` ✓ ověřeno |
| [Knihovna na vlnách: Aleš Kuda](https://www.mlp.cz/cz/novinky/knihovna-na-vlnach-ales-kuda) | Závislost je jen jedna – video na YouTube | `https://Závislost%20je%20jen%20jedna%20s%20adiktologem` | Místo adresy je v odkazu vložen text (název videa). Doplňte skutečnou adresu, nebo odkaz odstraňte. |
| [Loutky na scénu!](https://www.mlp.cz/cz/novinky/loutky-na-scenu) | Říši loutek | `https://www.riseloutek.cz/` | `https://www.riseloutek.cz/` |
| [Na hlavu 2026 se koná v Ústřední knihovně od 6. do 8. března](https://www.mlp.cz/cz/novinky/na-hlavu-2026-se-kona-v-ustredni-knihovne-od-6-do-8-brezna) | Koupit vstupenku | `/cz/ticketing/12558` | `https://www.mlp.cz/cz/ticketing/12558` ✓ ověřeno |
| [Novinky z Artotéky: leden 2026](https://www.mlp.cz/cz/novinky/novinky-z-artoteky-leden-2026) | Západ slnka | `/katalog/titul/zapad-slnka/504729` | `https://www.mlp.cz/katalog/titul/zapad-slnka/504729` ✓ ověřeno |
| [Pražské kolonky a čtvrť pod velkým mostem](https://www.mlp.cz/cz/novinky/prazske-kolonky-ctvrt-pod-velkym-mostem) | Oddělení pragensií | `https://o-knihovne/sluzby/specializovana-oddeleni/pragensia` | `https://www.mlp.cz/o-knihovne/sluzby/specializovana-oddeleni/pragensia` ✓ ověřeno |
| [Přípravný kurz k přijímacím zkouškám pro budoucí deváťáky](https://www.mlp.cz/cz/novinky/pripravny-kurz-k-prijimacim-zkouskam-pro-budouci-devataky) | Korunní | `//OREL/pobocky/korunni/` | `https://www.mlp.cz/pobocky/korunni/` ✓ ověřeno |
| [Rok slovenské hudby 2026: oslava slovenské hudební kultury](https://www.mlp.cz/cz/novinky/rok-slovenske-hudby-2026-oslava-slovenske-hudebni-kultury) | Hudobného centra | `www.hc.sk` | `www.hc.sk` |
| [S baterkou pod peřinou: ediční plán E-knihovny na jaro/léto…](https://www.mlp.cz/cz/novinky/s-baterkou-pod-perinou-edicni-plan-e-knihovny-na-jaroleto-2026) | Roberta Louise Stevensona | `https://katalog/osoba/stevenson-robert-louis/1189612?a_filter%5Bformat%5D%5Beq%5D=e-kniha&a_sort=rok` | `https://www.mlp.cz/katalog/osoba/stevenson-robert-louis/1189612?a_filter%5Bformat%5D%5Beq%5D=e-kniha&a_sort=r…` ✓ ověřeno |
| [Strom splněných přání 2026](https://www.mlp.cz/cz/novinky/strom-splnenych-prani-2026) | Obrázek | `https://www.dejmedetemsanci.cz/` | `https://www.dejmedetemsanci.cz/` |
| [Výměna pokojovek](https://www.mlp.cz/cz/novinky/vymena-pokojovek) | Barrandov. | `https://pobocky/barrandov/` | `https://www.mlp.cz/pobocky/barrandov/` ✓ ověřeno |
| [Povinné výtisky](https://www.mlp.cz/cz/o-knihovne/povinne-vytisky) | nakup@mlp.cz | `//OREL/User/rehakj/01_DRAMATURGIE%20WEB%20VÁLKA/2026/09_ZÁŘÍ/Povinný%20výtisk/nakup@mlp.cz` | `mailto:nakup@mlp.cz` |
| [Nabídka z fondu](https://www.mlp.cz/cz/o-knihovne/sluzby/knihovna-bez-barier/sluchove-znevyhodneni/nabidka-z-fondu) | České filmy | `https://katalog/davka/NFW-HAN-SLU-P-FIL-CES-DOS#/c_s_ol=espQCId-eq:NFW-HAN-SLU-P-FIL-CES-DOS-amp:navigation-e…` | `https://www.mlp.cz/katalog/davka/NFW-HAN-SLU-P-FIL-CES-DOS#/c_s_ol=espQCId-eq:NFW-HAN-SLU-P-FIL-CES-DOS-amp:n…` ✓ ověřeno |
| [Petřiny](https://www.mlp.cz/cz/pobocky/petriny) | Artotéky | `/o-knihovne/sluzby/specializovana-oddeleni/artoteka/,které` | `https://www.mlp.cz/o-knihovne/sluzby/specializovana-oddeleni/artoteka/` ✓ ověřeno |
| [Mobile library](https://www.mlp.cz/en/pobocky/mobile-library) | + | `tel:+` | Odkaz „tel:+“ neobsahuje číslo. Doplňte telefonní číslo nebo odkaz odstraňte. |
| [Mobile library](https://www.mlp.cz/en/pobocky/mobile-library) |  | `mailto:` | Odkaz „mailto:“ neobsahuje e-mailovou adresu. Doplňte ji nebo odkaz odstraňte. |
| [Mobile library](https://www.mlp.cz/en/pobocky/mobile-library) | Knihy v pohybu | `/cz/projekty/akce/knihy-v-pohybu/.(only` | `https://www.mlp.cz/cz/projekty/akce/knihy-v-pohybu/` |

<a id="old-url"></a>

## Stará / neexistující adresa na mlp.cz (34)

Priorita 1. Adresa na novém webu neexistuje (většinou adresa ze starého webu). Nahraďte ji navrženou adresou, nebo přes modul Redirect nastavte přesměrování.

| Kde | Text odkazu | Chybný odkaz | Navržená oprava |
|---|---|---|---|
| [Personal data protection](https://www.mlp.cz/en/services/personal-data-protection)<br>[Physical membership](https://www.mlp.cz/en/services/how-become-member/physical-membership)<br>[Online membership](https://www.mlp.cz/en/services/how-become-member/online-membership)<br>a dalších 1 | www.mlp.cz/en/branches / branches | `/en/branches/` |  |
| [Registrace do knihovny online pomocí Bank iD](https://www.mlp.cz/cz/novinky/registrace-do-knihovny-online-pomoci-bank-id)<br>[Physical membership](https://www.mlp.cz/en/services/how-become-member/physical-membership)<br>[Online membership](https://www.mlp.cz/en/services/how-become-member/online-membership) | VYPLNIT ONLINE PŘIHLÁŠKU / HERE / Become an online reader a… | `/moje-knihovna/` |  |
| [We are increasing the letter charges](https://www.mlp.cz/en/novinky/we-are-increasing-letter-charges-0)<br>[Pricelist](https://www.mlp.cz/en/services/pricelist) | Library Rules | `https://www.mlp.cz/en/about-us/library-rules/` | `https://www.mlp.cz/en/about-library/library-rules` ✓ ověřeno |
| [Physical card](https://www.mlp.cz/en/services/library-card/physical-card)<br>[Virtual library card](https://www.mlp.cz/en/services/library-card/virtual-library-card) | My account | `/en/muj-ucet/` | `https://www.mlp.cz/cz/napoveda/muj-ucet` ✓ ověřeno |
| [Dobrovolníci](https://www.mlp.cz/cz/kariera/dobrovolnici) | bibliobusu Oskar | `https://www.mlp.cz/cz/o-knihovne/pro-skoly/bibliobus-oskar/` | `https://www.mlp.cz/cz/o-knihovne/sluzby-pro-skoly/bibliobus-oskar` ✓ ověřeno |
| [Digitalizace pokračuje s novým skenerem](https://www.mlp.cz/cz/novinky/digitalizace-pokracuje-s-novym-skenerem) | www.mlp.cz/digitalizace | `http://www.mlp.cz/digitalizace` |  |
| [Divadelní a filmové oddělení na mezinárodním poli](https://www.mlp.cz/cz/novinky/divadelni-filmove-oddeleni-na-mezinarodnim-poli) | Divadelního a filmového oddělení | `https://www.mlp.cz/o-knihovne/sluzby/specializovana-oddeleni/divadelni-a-filmove-oddeleni/` | `https://www.mlp.cz/cz/o-knihovne/sluzby/specializovana-oddeleni/divadelni-filmove-oddeleni` ✓ ověřeno |
| [Nabitý podzim s Divadelním a filmovým oddělením](https://www.mlp.cz/cz/novinky/nabity-podzim-s-divadelnim-filmovym-oddelenim) | www.mlp.cz/divadleni | `http://www.mlp.cz/divadleni` |  |
| [Novinky z Artotéky: leden 2025](https://www.mlp.cz/cz/novinky/novinky-z-artoteky-leden-2025-0) | PŮJČTE SI | `/titul/5005648` |  |
| [Procházky Prahou: výstava obrazů Jitky Vackové](https://www.mlp.cz/cz/novinky/prochazky-prahou-vystava-obrazu-jitky-vackove) | Korunní | `/poocky/korunni/` | `https://www.mlp.cz/cz/pobocky/korunni` ✓ ověřeno |
| [Prodlužujeme zápis zdarma pro občany Ukrajiny](https://www.mlp.cz/cz/novinky/prodluzujeme-zapis-zdarma-pro-obcany-ukrajiny-0) | www.mlp.cz/ukrajina | `http://www.mlp.cz/ukrajina` |  |
| [Rok 2025: dostupnější pobočky i digitální gramotnost](https://www.mlp.cz/cz/novinky/rok-2025-dostupnejsi-pobocky-i-digitalni-gramotnost) | aplikace Knihovna | `/o-knihovne/online/mobilni-aplikace/` | `https://www.mlp.cz/cz/o-knihovne/sluzby-online/mobilni-aplikace` ✓ ověřeno |
| [Ústřední knihovna má víkendový provoz](https://www.mlp.cz/cz/novinky/ustredni-knihovna-ma-vikendovy-provoz) | Více o bezhotovostním placení a o službě peněžní záloha | `/napoveda/bezhotovostni-placeni-za-sluzby/` | `https://www.mlp.cz/cz/napoveda/bezhotovostni-placeni` ✓ ověřeno |
| [Visiolibrum - umění ve virtuální galerii](https://www.mlp.cz/cz/novinky/visiolibrum-umeni-ve-virtualni-galerii) | poboček | `https://www.mlp.cz/o-knihovne/sluzby/virtualni-realita/kam-na-vr/` | `https://www.mlp.cz/cz/o-knihovne/sluzby/virtualni-realita` ✓ ověřeno |
| [Zvyšení poplatků za dopis](https://www.mlp.cz/cz/novinky/zvyseni-poplatku-za-dopis) | Mém účtu | `/napoveda/ctenarske-konto-muj-ucet/` |  |
| [Athene a výroční zprávy](https://www.mlp.cz/cz/o-knihovne/povinne-informace-dokumenty/athene-vyrocni-zpravy) | Výroční zpráva za rok 2014 | `/cz/o-knihovne/cisla-dokumenty-povinne-informace/vyrocni-zpravy/vyrocni-zprava-2014/` |  |
| [Ochrana osobních údajů](https://www.mlp.cz/cz/o-knihovne/povinne-informace-dokumenty/ochrana-osobnich-udaju) | čtenářského účtu | `https://www.mlp.cz/moje-knihovna/` |  |
| [Ochrana osobních údajů](https://www.mlp.cz/cz/o-knihovne/povinne-informace-dokumenty/ochrana-osobnich-udaju) | Více informací zde >>> | `/o-knihovne/cisla-dokumenty-povinne-informace/povinne-dostupne-informace/cookies/` | `https://www.mlp.cz/cz/o-knihovne/povinne-informace-dokumenty/povinne-dostupne-informace/cookies` ✓ ověřeno |
| [Podrobné informace](https://www.mlp.cz/cz/o-knihovne/sluzby/specializovana-oddeleni/oddeleni-digitalizace/podrobne-informace) | Vzácných tisků | `https://www.mlp.cz/o-knihovne/sluzby/specializovana-oddeleni/vzacne-tisky/` | `https://www.mlp.cz/cz/o-knihovne/sluzby/specializovana-oddeleni/artoteka` ✓ ověřeno |
| [Podrobné informace](https://www.mlp.cz/cz/o-knihovne/sluzby/specializovana-oddeleni/oddeleni-digitalizace/podrobne-informace) | digitalizačním pracovištěm | `https://www.mlp.cz/o-knihovne/sluzby/specializovana-oddeleni/digitalizace/` | `https://www.mlp.cz/cz/o-knihovne/sluzby/specializovana-oddeleni/oddeleni-digitalizace` ✓ ověřeno |
| [Pragensia](https://www.mlp.cz/cz/o-knihovne/sluzby/specializovana-oddeleni/pragensia) | Wi-Fi | `/sluzby/internet-v-knihovne/` | `https://www.mlp.cz/cz/o-knihovne/sluzby/internet-v-knihovne` ✓ ověřeno |
| [Kobylisy](https://www.mlp.cz/cz/pobocky/kobylisy) | Pravidla pro používání internetu | `https://www.mlp.cz/cz/akce/e35333-vysivani/` |  |
| [Vysočany](https://www.mlp.cz/cz/pobocky/vysocany) | Pravidla pro používání internetu | `/o-knihovne/sluzby/internet-v-knihovne/¨` | `https://www.mlp.cz/cz/o-knihovne/sluzby/internet-v-knihovne` ✓ ověřeno |
| [Idiom](https://www.mlp.cz/en/about-library/idiom) | Central Library | `/en/branches/central-library/` | `https://www.mlp.cz/en/pobocky/central-library` ✓ ověřeno |
| [We are increasing the letter charges](https://www.mlp.cz/en/novinky/we-are-increasing-letter-charges-0) | branches | `https://www.mlp.cz/en/branches/` |  |
| [Brusnice - vzácné tisky](https://www.mlp.cz/en/pobocky/brusnice-vzacne-tisky) | PODROBNÉ INFORMACE | `https://www.mlp.cz/cz/pobocky/brusnice-vzacne-tisky/novinky/1146-podrobne-informace/` |  |
| [Central Library](https://www.mlp.cz/en/pobocky/central-library) | www.mlp.cz/en/branches/ | `http://www.mlp.cz/en/branches/` |  |
| [Central Library](https://www.mlp.cz/en/pobocky/central-library) | Idiom – column made of 8,000 books | `https://www.mlp.cz/en/events-and-news/1416-idiom/` |  |
| [Jezerka](https://www.mlp.cz/en/pobocky/jezerka) | Pobočka je monitorována kamerovým systémem | `https://www.mlp.cz/cz/o-knihovne/cisla-dokumenty-povinne-informace/ochrana-osobnich-udaju/` | `https://www.mlp.cz/cz/o-knihovne/povinne-informace-dokumenty/ochrana-osobnich-udaju` ✓ ověřeno |
| [Mobile library](https://www.mlp.cz/en/pobocky/mobile-library) | branch | `http://www.mlp.cz/en/branches-and-contacts/branches/` |  |
| [Mobile library](https://www.mlp.cz/en/pobocky/mobile-library) | TIMETABLE in czech | `/cz/kontakty/bibliobus/` |  |
| [Mobile library](https://www.mlp.cz/en/pobocky/mobile-library) | public library | `/cz/o-knihovne/knihovnam-v-praze/` | `https://www.mlp.cz/cz/o-knihovne/knihovni-rad` ✓ ověřeno |
| [Mobile library](https://www.mlp.cz/en/pobocky/mobile-library) | bibliobuses | `http://www.mlp.cz/en/branches-and-contacts/book-bus/` |  |
| [Physical membership](https://www.mlp.cz/en/services/how-become-member/physical-membership) | HERE | `/en/1553-online-membership/` |  |

<a id="old-domain"></a>

## Odkaz na starý / testovací web knihovny (12)

Priorita 1. Odkazy na starý / testovací web knihovny (old.mlp.cz, demo.mlp.cz, wwwbeta.mlp.cz, l.mlp.cz), který už nefunguje. Nahraďte odkazem na stránku na www.mlp.cz, nebo odkaz odstraňte.

| Kde | Text odkazu | Chybný odkaz |
|---|---|---|
| [PressReader nově dostupný i z domova](https://www.mlp.cz/cz/novinky/pressreader-nove-dostupny-i-z-domova)<br>[Věda, noviny, časopisy](https://www.mlp.cz/cz/o-knihovne/sluzby/e-zdroje/veda-noviny-casopisy)<br>[Databáze na pobočkách](https://www.mlp.cz/cz/o-knihovne/sluzby/e-zdroje/databaze-na-pobockach) | Vstup do databáze PressReader / Vstup do databáze | `http://l.mlp.cz/pressreader` |
| [Projekt Bookstart na našich pobočkách](https://www.mlp.cz/cz/novinky/projekt-bookstart-na-nasich-pobockach) | Lužiny | `https://old.mlp.cz/pobocky/luziny/` |
| [Projekt Bookstart na našich pobočkách](https://www.mlp.cz/cz/novinky/projekt-bookstart-na-nasich-pobockach) | Stodůlky | `https://old.mlp.cz/pobocky/stodulky/` |
| [Rychlá platba kartou v samoobslužné pokladně](https://www.mlp.cz/cz/novinky/rychla-platba-kartou-v-samoobsluzne-pokladne) | Barrandov | `https://demo.mlp.cz/pobocky/barrandov/` |
| [Rychlá platba kartou v samoobslužné pokladně](https://www.mlp.cz/cz/novinky/rychla-platba-kartou-v-samoobsluzne-pokladne) | Lužiny | `https://demo.mlp.cz/pobocky/luziny/` |
| [Rychlá platba kartou v samoobslužné pokladně](https://www.mlp.cz/cz/novinky/rychla-platba-kartou-v-samoobsluzne-pokladne) | Ústřední knihovna | `https://demo.mlp.cz/pobocky/ustredni-knihovna/` |
| [Rychlá platba kartou v samoobslužné pokladně](https://www.mlp.cz/cz/novinky/rychla-platba-kartou-v-samoobsluzne-pokladne) | Velký mlýn | `https://demo.mlp.cz/pobocky/velky-mlyn/` |
| [Rychlá platba kartou v samoobslužné pokladně](https://www.mlp.cz/cz/novinky/rychla-platba-kartou-v-samoobsluzne-pokladne) | Kiosek CČM | `https://demo.mlp.cz/pobocky/kiosek-ccm/` |
| [Rychlá platba kartou v samoobslužné pokladně](https://www.mlp.cz/cz/novinky/rychla-platba-kartou-v-samoobsluzne-pokladne) | Kiosek DBK | `https://demo.mlp.cz/pobocky/kiosek-dbk/` |
| [Rychlá platba kartou v samoobslužné pokladně](https://www.mlp.cz/cz/novinky/rychla-platba-kartou-v-samoobsluzne-pokladne) | Kiosek Chodov | `https://demo.mlp.cz/pobocky/kiosek-chodov/` |
| [Praha město literatury](https://www.mlp.cz/cz/o-knihovne/praha-mesto-literatury) | Městská knihovna v Praze | `http://wwwbeta.mlp.cz/cz/` |
| [Nabídka z fondu](https://www.mlp.cz/cz/o-knihovne/sluzby/knihovna-bez-barier/pohybove-znevyhodneni/nabidka-z-fondu) | Naučnou literaturu o problematice pohybového znevýhodnění | `https://demo.mlp.cz/katalog/davka/NFW_POHYB_HANDICAP?p=#/c_s_ol=espQCId-eq:NFW_POHYB_HANDICAP` |

<a id="document"></a>

## Chybějící dokument / soubor (11)

Priorita 1. Odkazovaný dokument (PDF) neexistuje – hlavně staré odkazy `/cz/dokumenty/?act=get…`. Nahrajte dokument do Médií a odkaz nahraďte, nebo ho odstraňte.

| Kde | Text odkazu | Chybný odkaz |
|---|---|---|
| [Kulturní program na červen 2026](https://www.mlp.cz/cz/novinky/kulturni-program-na-cerven-2026) | Program Kina Petřiny | `https://www.mlp.cz/sites/mlp.cz/files/2026-05/kino_petriny_cerven_2026.pdf` |
| [O knihovnickou sovu 2025](https://www.mlp.cz/cz/novinky/o-knihovnickou-sovu-2025) | Stáhněte si všechny potřebné informace! | `https://www.mlp.cz/cz/dokumenty/?act=get&check=240ff837cc0d6d76a2bec920cd1f2d7c&id=2978&noinc=1` |
| [Prodlužujeme zápis zdarma pro občany Ukrajiny](https://www.mlp.cz/cz/novinky/prodluzujeme-zapis-zdarma-pro-obcany-ukrajiny-0) | Registrace občanů Ukrajiny – Zvláštní dodatek ke Knihovnímu… | `https://www.mlp.cz/cz/dokumenty/?act=get&check=c329a96b0817c62f26678fc4f43f8743&id=2729&noinc=1` |
| [Zápis do knihovny zdarma pro občany Ukrajiny](https://www.mlp.cz/cz/novinky/zapis-do-knihovny-zdarma-pro-obcany-ukrajiny) | Registrace občanů Ukrajiny | `https://www.mlp.cz/cz/dokumenty/?act=get&check=d18f2321fe2054e3c2ee8ab541f45493&id=2607&noinc=1` |
| [Rok 2026](https://www.mlp.cz/cz/o-knihovne/povinne-informace-dokumenty/archiv-tiskovych-zprav/rok-2026) | Konference - knihovny jako místa digitálního vzdělávání | `/sites/mlp.cz/files/2026-02/konference-predstavuje-knihovny-jako-mista-digitalniho-vzdelavani.pdf` |
| [Virtuální realita](https://www.mlp.cz/cz/o-knihovne/sluzby/virtualni-realita) | Projekt virtuální reality v Městské knihovně v Praze | `https://www.mlp.cz/cz/dokumenty/?act=get&check=942919db16d9e0e0a8c5285e71db6b5e&id=2877&noinc=1` |
| [Virtuální realita](https://www.mlp.cz/cz/o-knihovne/sluzby/virtualni-realita) | Podrobné informace o kontraindikacích | `https://www.mlp.cz/cz/dokumenty/?act=get&check=d3b0892de135042a0eb6271ccd591fb0&id=2879&noinc=1` |
| [Virtuální realita](https://www.mlp.cz/cz/o-knihovne/sluzby/virtualni-realita) | Health and safety recommendation VR | `https://www.mlp.cz/cz/dokumenty/?act=get&check=ad419c211e22c6c98662156951178d6a&id=2880&noinc=1` |
| [Jezerka](https://www.mlp.cz/en/pobocky/jezerka) | Nabídka online programů pro školy | `/cz/dokumenty/?act=get&check=ea7a085858d1d2daf5dd56a64d82d2a4&id=2504&noinc=1` |
| [Jezerka](https://www.mlp.cz/en/pobocky/jezerka) | Nabídka besed pro školy | `/cz/dokumenty/?act=get&check=45f0cb73bbcee6df92a51135dbc4a8db&id=2765&noinc=1` |
| [Mobile library](https://www.mlp.cz/en/pobocky/mobile-library) | TIMETABLE in PDF czech version | `/cz/dokumenty/?act=get&check=6037e7b126d2b6645c4b9e154155003f&id=707&noinc=1` |

<a id="unpublished"></a>

## Odkaz na nepublikovaný článek (9)

Priorita 1. Odkaz vede na nepublikovaný článek, návštěvník uvidí „Přístup odepřen“. Článek publikujte, nebo odkaz odstraňte.

| Kde | Text odkazu | Chybný odkaz |
|---|---|---|
| [Bohnice](https://www.mlp.cz/cz/pobocky/bohnice)<br>[Dejvice](https://www.mlp.cz/cz/pobocky/dejvice)<br>[Kobylisy](https://www.mlp.cz/cz/pobocky/kobylisy)<br>a dalších 2 | Výměna rostlin | `/novinky/vymena-rostlin-swap` |
| [Co čeká knihovnu v roce 2026](https://www.mlp.cz/cz/novinky/co-ceka-knihovnu-v-roce-2026) | redesignovaných webových stránek | `/cz/novinky/testujte-novy-web` |
| [Jak máme zavřeno v roce 2026](https://www.mlp.cz/cz/novinky/jak-mame-zavreno-v-roce-2026) | Dejvice | `https://www.mlp.cz/cz/novinky/pobocka-dejvice-uzavrena-v-sobotu-2-5-2026` |
| [Jak máme zavřeno v roce 2026](https://www.mlp.cz/cz/novinky/jak-mame-zavreno-v-roce-2026) | pobočka Lužiny bude uzavřena | `https://www.mlp.cz/cz/novinky/pobocka-luziny-uzavrena-od-4-5-do-16-5-2026` |
| [Týden 17: sdílená krajina](https://www.mlp.cz/cz/novinky/tyden-17-sdilena-krajina) | Hrnkobraní na Korunní – swap hrnečků | `https://www.mlp.cz/cz/novinky/hrnkobrani-na-korunni-swap-hrnecku` |
| [Bohnice](https://www.mlp.cz/cz/pobocky/bohnice) | Doučování v knihovně | `/novinky/doucovani-v-bohnicich` |
| [Brusnice - vzácné tisky](https://www.mlp.cz/cz/pobocky/brusnice-vzacne-tisky) | PODROBNÉ INFORMACE | `/novinky/vzacne-tisky-podrobne-informace` |
| [Modřany](https://www.mlp.cz/cz/pobocky/modrany) | Doučování v knihovně | `/novinky/doucovani-v-knihovne-zabavne-zdarma` |
| [Školská](https://www.mlp.cz/cz/pobocky/skolska) | knihobudky | `/novinky/knihobudka` |

<a id="lang-switch"></a>

## Přepínač jazyka EN vede na 404 (1)

Priorita 1. Na českých stránkách bez anglického překladu vede přepínač „EN“ v hlavičce na `/en/…` se stejnou cestou, což končí chybou 404. **Oprava pro správce webu:** u stránek bez překladu přepínač skrýt, nebo ho nasměrovat na https://www.mlp.cz/en.

Týká se 198 stránek, např. [/cz/o-knihovne](https://www.mlp.cz/cz/o-knihovne), [/cz/kariera](https://www.mlp.cz/cz/kariera), [/cz/napoveda](https://www.mlp.cz/cz/napoveda), [/cz/o-knihovne/sluzby](https://www.mlp.cz/cz/o-knihovne/sluzby), [/cz/o-knihovne/sluzby-pro-obcany-ukrajiny](https://www.mlp.cz/cz/o-knihovne/sluzby-pro-obcany-ukrajiny). Úplný seznam je v tabulce `opravy.xlsx`.

<a id="external-404"></a>

## Cizí web: stránka neexistuje (404) (25)

Priorita 2. Stránka na cizím webu byla zrušena nebo přesunuta. Najděte novou adresu, nebo odkaz odstraňte.

| Kde | Text odkazu | Chybný odkaz | Navržená oprava |
|---|---|---|---|
| [Organizace a spolky](https://www.mlp.cz/cz/o-knihovne/sluzby/knihovna-bez-barier/zrakove-znevyhodneni/organizace-spolky)<br>[Organizace a spolky](https://www.mlp.cz/cz/o-knihovne/sluzby/knihovna-bez-barier/sluchove-znevyhodneni/organizace-spolky) | www.lorm.cz/…ktuality.php | `http://www.lorm.cz/cs/lorm/aktuality.php` |  |
| [Dobrovolníci](https://www.mlp.cz/cz/kariera/dobrovolnici) | https://dofe.cz/ | `https://dofe.cz/_` |  |
| [Elvis Presley](https://www.mlp.cz/cz/novinky/elvis-presley) | https://commons.wikimedia.org/…Elvis-nixon_ | `https://commons.wikimedia.org/wiki/File:Elvis-nixon_` |  |
| [Mariánská listování: Zdeněk Jurásek](https://www.mlp.cz/cz/novinky/marianska-listovani-zdenek-jurasek) | YouTube | `https://www.youtube.com/@mestskaknihovnavpraze` | `https://www.youtube.com/@KnihovnaPraha` |
| [Visiolibrum - umění ve virtuální galerii](https://www.mlp.cz/cz/novinky/visiolibrum-umeni-ve-virtualni-galerii) | Virtual Reality | `https://commons.wikimedia.org/wiki/File:VR-AR-XR_Headset_3.jpg` |  |
| [Athene a výroční zprávy](https://www.mlp.cz/cz/o-knihovne/povinne-informace-dokumenty/athene-vyrocni-zpravy) | Výroční časopis Athene 2019 | `https://issuu.com/home/published/athene_2019` |  |
| [Athene a výroční zprávy](https://www.mlp.cz/cz/o-knihovne/povinne-informace-dokumenty/athene-vyrocni-zpravy) | Výroční časopis Athene 2017 | `https://issuu.com/home/published/athene_2017_digi` |  |
| [Praha město literatury](https://www.mlp.cz/cz/o-knihovne/praha-mesto-literatury) | Kreativních měst literatury UNESCO | `https://www.prahamestoliteratury.cz/cz/o-projektu/kreativni-mesta-literatury-unesco/` |  |
| [Praha město literatury](https://www.mlp.cz/cz/o-knihovne/praha-mesto-literatury) | Kreativní rezidenční pobyty pro zahraniční spisovatele a př… | `https://www.prahamestoliteratury.cz/cz/aktivity/rezidencni-pobyty/` |  |
| [Praha město literatury](https://www.mlp.cz/cz/o-knihovne/praha-mesto-literatury) | Básník města / Básnířka města | `https://www.prahamestoliteratury.cz/cz/aktivity/basnirka-mesta-prahy/` |  |
| [Praha město literatury](https://www.mlp.cz/cz/o-knihovne/praha-mesto-literatury) | Autorská čtení Doteky světové literatury | `https://www.prahamestoliteratury.cz/cz/aktivity/doteky-svetove-literatury/` |  |
| [Praha město literatury](https://www.mlp.cz/cz/o-knihovne/praha-mesto-literatury) | Kalendář kulturních akcí | `https://www.prahamestoliteratury.cz/cz/udalosti/` |  |
| [Praha město literatury](https://www.mlp.cz/cz/o-knihovne/praha-mesto-literatury) | Knihy z Prahy | `https://www.prahamestoliteratury.cz/cz/aktivity/knihy-z-prahy/` |  |
| [Praha město literatury](https://www.mlp.cz/cz/o-knihovne/praha-mesto-literatury) | webových stránek | `https://www.prahamestoliteratury.cz/cz/` |  |
| [Organizace a spolky](https://www.mlp.cz/cz/o-knihovne/sluzby/knihovna-bez-barier/mentalne-znevyhodneni/organizace-spolky) | http://www.parkinson-cz.net/forum3/ | `http://www.parkinson-cz.net/forum3/` |  |
| [Organizace a spolky](https://www.mlp.cz/cz/o-knihovne/sluzby/knihovna-bez-barier/sluchove-znevyhodneni/organizace-spolky) | www.okamzik.cz/…A/index.html | `http://www.okamzik.cz/main/okamzik/VIA/index.html` |  |
| [Organizace a spolky](https://www.mlp.cz/cz/o-knihovne/sluzby/knihovna-bez-barier/zrakove-znevyhodneni/organizace-spolky) | www.ktn.cz/index | `http://www.ktn.cz/index` |  |
| [Organizace a spolky](https://www.mlp.cz/cz/o-knihovne/sluzby/knihovna-bez-barier/zrakove-znevyhodneni/organizace-spolky) | www.spektravox.cz/cs/zrakove-vady | `http://www.spektravox.cz/cs/zrakove-vady` |  |
| [Organizace a spolky](https://www.mlp.cz/cz/o-knihovne/sluzby/knihovna-bez-barier/zrakove-znevyhodneni/organizace-spolky) | www.volny.cz/timsel/ | `http://www.volny.cz/timsel/` |  |
| [Doporučujeme na internetu](https://www.mlp.cz/cz/o-knihovne/sluzby/specializovana-oddeleni/hudebni-oddeleni/doporucujeme-na-internetu) | http://www.ceskyhudebnislovnik.cz/slovnik/ | `http://www.ceskyhudebnislovnik.cz/slovnik/` |  |
| [Doporučujeme na internetu](https://www.mlp.cz/cz/o-knihovne/sluzby/specializovana-oddeleni/hudebni-oddeleni/doporucujeme-na-internetu) | http://www.czech-music.net/cs | `http://www.czech-music.net/cs` |  |
| [Doporučujeme na internetu](https://www.mlp.cz/cz/o-knihovne/sluzby/specializovana-oddeleni/hudebni-oddeleni/doporucujeme-na-internetu) | http://www.muzikus.cz/…is-harmonie/ | `http://www.muzikus.cz/casopis-harmonie/` |  |
| [Doporučujeme na internetu](https://www.mlp.cz/cz/o-knihovne/sluzby/specializovana-oddeleni/hudebni-oddeleni/doporucujeme-na-internetu) | http://www.lib.cas.cz/…udebni-veda/ | `http://www.lib.cas.cz/publikacni-cinnost/prehled-casopisu-vydavanych-v-av-cr/hudebni-veda/` |  |
| [Doporučujeme na internetu](https://www.mlp.cz/cz/o-knihovne/sluzby/specializovana-oddeleni/hudebni-oddeleni/doporucujeme-na-internetu) | http://www.nm.cz/…e-detail.php?… | `http://www.nm.cz/publikace/publikace-detail.php?id=16` |  |
| [Kino MKP](https://www.mlp.cz/cz/o-knihovne/sluzby/specializovana-oddeleni/kulturni-vzdelavaci-centrum/kino-mkp) | Asociace českých filmových klubů | `http://www.acfk.cz/homepage/` |  |

<a id="image"></a>

## Nefunkční obrázek ze starého webu (19)

Priorita 2. Obrázky vložené ze starého webu (`/noRW_photodisplay/…`) se nezobrazují. Nahrajte je znovu do Médií, nebo je z článku odstraňte.

| Kde | Text odkazu | Chybný odkaz |
|---|---|---|
| [Artotéka Open Call 2026](https://www.mlp.cz/cz/novinky/artoteka-open-call-2026) | (Super Admin) | `Obrázky ze starého webu (15 ks), např. https://www.mlp.cz/noRW_photodisplay/24/39639_24e94a0adc7874875b7a8f9a…` |
| [Děti světu – Den dětí jinak](https://www.mlp.cz/cz/novinky/deti-svetu-den-deti-jinak) |  | `Obrázky ze starého webu (4 ks), např. https://old.mlp.cz/noRW_photodisplay/02/38320_0269d866e8e122e1e79e75294…` |
| [Divadelní a filmové oddělení a komunita](https://www.mlp.cz/cz/novinky/divadelni-filmove-oddeleni-komunita) |  | `Obrázky ze starého webu (5 ks), např. https://www.mlp.cz/noRW_photodisplay/65/34606_65ea8a7117696440c166cef0b…` |
| [Do černého: 26. ledna 2026 v Ústřední knihovně](https://www.mlp.cz/cz/novinky/do-cerneho-26-ledna-2026-v-ustredni-knihovne) |  | `https://www.mlp.cz/noRW_photodisplay/c0/40049_c09f3cb63710d6f65c0b1d90d2e6e16e.jpg` |
| [Eric Clapton](https://www.mlp.cz/cz/novinky/eric-clapton) |  | `Obrázky ze starého webu (6 ks), např. https://www.mlp.cz/noRW_photodisplay/d7/37593_d7c4955a2be8097435a651e45…` |
| [Francouzské fikce a myšlenky](https://www.mlp.cz/cz/novinky/francouzske-fikce-myslenky) |  | `Obrázky ze starého webu (8 ks), např. https://www.mlp.cz/noRW_photodisplay/17/36795_176be20982468f00de6d4f2ed…` |
| [Hudební novinky: leden 2025](https://www.mlp.cz/cz/novinky/hudebni-novinky-leden-2025-0) |  | `Obrázky ze starého webu (3 ks), např. https://www.mlp.cz/noRW_photodisplay/7d/36565_7d97b2283f8148e65172ad0dd…` |
| [Jan Lukavec: Jižní Město 2061](https://www.mlp.cz/cz/novinky/jan-lukavec-jizni-mesto-2061) |  | `https://www.mlp.cz/noRW_photodisplay/28/28709_287afd7c0b1cd3b1454b841a329cc3ef.jpg` |
| [Mami, tati, dějou se věci 2025](https://www.mlp.cz/cz/novinky/mami-tati-dejou-se-veci-2025) |  | `Obrázky ze starého webu (3 ks), např. https://old.mlp.cz/noRW_photodisplay/f2/38429_f24d5e23a8b3b9dcce8deb327…` |
| [Novinky z Artotéky: leden 2025](https://www.mlp.cz/cz/novinky/novinky-z-artoteky-leden-2025-0) |  | `https://www.mlp.cz/noRW_photodisplay/82/36634_82a3e526e02b1152b5664004fd46a38e.jpg` |
| [Pražský rezidenční program 2015-2025](https://www.mlp.cz/cz/novinky/prazsky-rezidencni-program-2015-2025) |  | `Obrázky ze starého webu (10 ks), např. https://www.mlp.cz/noRW_photodisplay/23/36719_2382e5436ca6edc376c9ac26…` |
| [Rozhovor: Věra Ryšavá a Daniela Jelínková](https://www.mlp.cz/cz/novinky/rozhovor-vera-rysava-daniela-jelinkova) |  | `https://www.mlp.cz/noRW_photodisplay/03/28661_03efc465ef0589342d81bc4333b5625a.jpg` |
| [Ústřední knihovna má víkendový provoz](https://www.mlp.cz/cz/novinky/ustredni-knihovna-ma-vikendovy-provoz) |  | `Obrázky ze starého webu (2 ks), např. https://www.mlp.cz/noRW_photodisplay/9a/38723_9a26f20c6ce037fb0232796bf…` |
| [Visiolibrum - umění ve virtuální galerii](https://www.mlp.cz/cz/novinky/visiolibrum-umeni-ve-virtualni-galerii) |  | `Obrázky ze starého webu (3 ks), např. https://www.mlp.cz/noRW_photodisplay/33/37514_338a04f7efaf095a8341595b5…` |
| [Vyplatí se knihovna](https://www.mlp.cz/cz/novinky/vyplati-se-knihovna) |  | `https://old.mlp.cz/noRW_photodisplay/f7/17514_f7995706ecd8a5a2cec9a030703878d6.jpg` |
| [Podrobné informace](https://www.mlp.cz/cz/o-knihovne/sluzby/specializovana-oddeleni/oddeleni-digitalizace/podrobne-informace) |  | `https://www.mlp.cz/noRW_photodisplay/8b/19939_8bb9623c13ae61c3a2800d8d76cc365f.png` |
| [The Central Library is open on weekends](https://www.mlp.cz/en/novinky/central-library-open-weekends) |  | `Obrázky ze starého webu (2 ks), např. https://www.mlp.cz/noRW_photodisplay/9a/38723_9a26f20c6ce037fb0232796bf…` |
| [Year 2025: more accessible branches and digital literacy](https://www.mlp.cz/en/novinky/year-2025-more-accessible-branches-and-digital-literacy-0) |  | `Obrázky ze starého webu (3 ks), např. https://www.mlp.cz/noRW_photodisplay/a0/36506_a0112fae7d18ebe0276e5d101…` |
| [Physical card](https://www.mlp.cz/en/services/library-card/physical-card) | (Jakub ŘEHÁK) | `Obrázky ze starého webu (8 ks), např. https://www.mlp.cz/noRW_photodisplay/c7/24808_c75184387f83f9f9312dcd589…` |

<a id="catalog"></a>

## Neexistující záznam v katalogu (1)

Priorita 2. Záznam v katalogu neexistuje. Vyhledejte titul znovu a odkaz aktualizujte.

| Kde | Text odkazu | Chybný odkaz | Navržená oprava |
|---|---|---|---|
| [Zlé roky pražské dopravy](https://www.mlp.cz/cz/novinky/zle-roky-prazske-dopravy) | novinky v katalogu | `/davka/NFW_WPRAG_NOVINKY_05_25?p=#/c_s_ol=espQCId-eq:%20NFW_WPRAG_NOVINKY_05_25` | `https://www.mlp.cz/katalog/davka/NFW_WPRAG_NOVINKY_05_25?p=` ✓ ověřeno |

<a id="event"></a>

## Smazaná akce (1)

Priorita 2. Akce byla smazána. Odkaz odstraňte nebo nahraďte.

| Kde | Text odkazu | Chybný odkaz |
|---|---|---|
| [Týden pro Knihovny.Digital](https://www.mlp.cz/cz/novinky/tyden-pro-knihovnydigital) | 3. 11. 2026 - 15:00–⁠⁠⁠⁠⁠18:00 - Ústřední knihovna - Knihov… | `https://www.mlp.cz/cz/akce/knihovna-jinak-virtualni-prochazka/12962` |

<a id="external-dead"></a>

## Cizí web nedostupný / zaniklý (42)

Priorita 3. Cizí web se opakovaně (třikrát) nepodařilo načíst – pravděpodobně zanikl. Ověřte v prohlížeči a případně odkaz odstraňte.

| Kde | Text odkazu | Chybný odkaz |
|---|---|---|
| [100 let značky Odeon](https://www.mlp.cz/cz/novinky/100-let-znacky-odeon)<br>[S baterkou pod peřinou: ediční plán E-knihovny na jaro/léto…](https://www.mlp.cz/cz/novinky/s-baterkou-pod-perinou-edicni-plan-e-knihovny-na-jaroleto-2026)<br>[Trojí ohlédnutí za tzv. Šestatřicátníky](https://www.mlp.cz/cz/novinky/troji-ohlednuti-za-tzv-sestatricatniky)<br>a dalších 1 | www.e-knihovna.cz / E-knihovny | `https://www.e-knihovna.cz/` |
| [Moře k moři](https://www.mlp.cz/cz/novinky/more-k-mori)<br>[Studujte v knihovně](https://www.mlp.cz/cz/novinky/studujte-v-knihovne) | www.e-knihovna.cz | `https://www.e-knihovna.cz` |
| [E-knihy](https://www.mlp.cz/cz/o-knihovne/sluzby/e-zdroje/e-knihy)<br>[KnihDoKaps – čtečky pro seniory](https://www.mlp.cz/cz/o-knihovne/sluzby/pro-seniory/knihdokaps-ctecky-pro-seniory) | www.e-knihovna.cz | `http://www.e-knihovna.cz` |
| [Desatero komunikace](https://www.mlp.cz/cz/o-knihovne/sluzby/knihovna-bez-barier/pohybove-znevyhodneni/desatero-komunikace)<br>[Desatero komunikace](https://www.mlp.cz/cz/o-knihovne/sluzby/knihovna-bez-barier/mentalne-znevyhodneni/desatero-komunikace) | http://www.kr-olomoucky.cz | `http://www.kr-olomoucky.cz` |
| [Knihy](https://www.mlp.cz/cz/o-knihovne/sluzby/knihy)<br>[Oddělení digitalizace](https://www.mlp.cz/cz/o-knihovne/sluzby/specializovana-oddeleni/oddeleni-digitalizace) | http://www.e-knihovna.cz/ / www.e-knihovna.cz | `http://www.e-knihovna.cz/` |
| [Brusnice - vzácné tisky](https://www.mlp.cz/cz/pobocky/brusnice-vzacne-tisky)<br>[Brusnice - vzácné tisky](https://www.mlp.cz/en/pobocky/brusnice-vzacne-tisky) | Pražská plynárenská | `https://www.ppas.cz/` |
| [Hloubětín](https://www.mlp.cz/cz/pobocky/hloubetin)<br>[Hloubětín](https://www.mlp.cz/en/pobocky/hloubetin) | H55 | `https://www.h55.cz/` |
| [Hloubětín](https://www.mlp.cz/cz/pobocky/hloubetin)<br>[Hloubětín](https://www.mlp.cz/en/pobocky/hloubetin) | H55 | `//www.h55.cz/` |
| [Městská knihovna v Praze](https://www.mlp.cz/) | Design by | `http://www.2fresh.cz` |
| [Ediční plán E-knihovny: podzim/zima 2026](https://www.mlp.cz/cz/novinky/edicni-plan-e-knihovny-podzimzima-2026) | E-knihovny.cz | `http://e-knihovny.cz` |
| [Knihovna na vlnách: multižánrový festival probíhá do 16. 7.…](https://www.mlp.cz/cz/novinky/knihovna-na-vlnach-multizanrovy-festival-probiha-do-16-7-2026) | https://martinastara.cz/ | `https://martinastara.cz/` |
| [Rozhovor: Věra Ryšavá a Daniela Jelínková](https://www.mlp.cz/cz/novinky/rozhovor-vera-rysava-daniela-jelinkova) | Reportáž o výročí na PRAHA TV | `https://prahatv.eu/zpravy/praha/praha-11/17961/mestska-knihovna-opatov-oslavila-40-narozeniny` |
| [Teatrologická společnost slaví úspěchy](https://www.mlp.cz/cz/novinky/teatrologicka-spolecnost-slavi-uspechy) | http://rvs.paleontologie.cz/ | `http://rvs.paleontologie.cz/` |
| [Zažít město jinak 2026: sousedské slavnosti na našich poboč…](https://www.mlp.cz/cz/novinky/zazit-mesto-jinak-2026-sousedske-slavnosti-na-nasich-pobockach) | https://zazitmestojinak.cz/ | `https://zazitmestojinak.cz/` |
| [Partneři](https://www.mlp.cz/cz/o-knihovne/partneri) | www.ppas.cz | `http://www.ppas.cz/` |
| [Projekt CENTRAL](https://www.mlp.cz/cz/o-knihovne/sluzby-pro-knihovny/projekt-central) | Souborného katalogu ČR ostatním knihovnám | `https://aleph.nkp.cz/F/?func=file&file_name=base-list` |
| [Projekt CENTRAL](https://www.mlp.cz/cz/o-knihovne/sluzby-pro-knihovny/projekt-central) | informace zde | `http://aleph.nkp.cz/web/z3950_cze.htm` |
| [Webové knihy](https://www.mlp.cz/cz/o-knihovne/sluzby/e-zdroje/webove-knihy) | e-knihovna.cz | `http://e-knihovna.cz/` |
| [Organizace a spolky](https://www.mlp.cz/cz/o-knihovne/sluzby/knihovna-bez-barier/mentalne-znevyhodneni/organizace-spolky) | http://www.autistik.cz/ | `http://www.autistik.cz/` |
| [Organizace a spolky](https://www.mlp.cz/cz/o-knihovne/sluzby/knihovna-bez-barier/mentalne-znevyhodneni/organizace-spolky) | http://www.uzps.cz | `http://www.uzps.cz` |
| [Organizace a spolky](https://www.mlp.cz/cz/o-knihovne/sluzby/knihovna-bez-barier/mentalne-znevyhodneni/organizace-spolky) | http://www.domovdana.cz/ | `http://www.domovdana.cz/` |
| [Organizace a spolky](https://www.mlp.cz/cz/o-knihovne/sluzby/knihovna-bez-barier/mentalne-znevyhodneni/organizace-spolky) | http://www.mameotevreno.cz/html/ | `http://www.mameotevreno.cz/html/` |
| [Organizace a spolky](https://www.mlp.cz/cz/o-knihovne/sluzby/knihovna-bez-barier/mentalne-znevyhodneni/organizace-spolky) | http://www.parity.cz/ | `http://www.parity.cz/` |
| [Organizace a spolky](https://www.mlp.cz/cz/o-knihovne/sluzby/knihovna-bez-barier/mentalne-znevyhodneni/organizace-spolky) | http://www.simp.cz/ | `http://www.simp.cz/` |
| [Organizace a spolky](https://www.mlp.cz/cz/o-knihovne/sluzby/knihovna-bez-barier/pohybove-znevyhodneni/organizace-spolky) | http://www.osboruvka.cz/ | `http://www.osboruvka.cz/` |
| [Organizace a spolky](https://www.mlp.cz/cz/o-knihovne/sluzby/knihovna-bez-barier/pohybove-znevyhodneni/organizace-spolky) | http://www.fragilnix.cz/ | `http://www.fragilnix.cz/` |
| [Organizace a spolky](https://www.mlp.cz/cz/o-knihovne/sluzby/knihovna-bez-barier/pohybove-znevyhodneni/organizace-spolky) | http://www.antee.cz/…ko/index.php?… | `http://www.antee.cz/klubkolecko/index.php?nid=8233&lid=CS&oid=1551245` |
| [Organizace a spolky](https://www.mlp.cz/cz/o-knihovne/sluzby/knihovna-bez-barier/sluchove-znevyhodneni/organizace-spolky) | www.ticho.cz/osoba.php?… | `http://www.ticho.cz/osoba.php?xtem=&key=8` |
| [Organizace a spolky](https://www.mlp.cz/cz/o-knihovne/sluzby/knihovna-bez-barier/sluchove-znevyhodneni/organizace-spolky) | www.jablickodetem.cz/ | `http://www.jablickodetem.cz/` |
| [Organizace a spolky](https://www.mlp.cz/cz/o-knihovne/sluzby/knihovna-bez-barier/sluchove-znevyhodneni/organizace-spolky) | www.neslysici.cz | `http://www.neslysici.cz` |
| [Organizace a spolky](https://www.mlp.cz/cz/o-knihovne/sluzby/knihovna-bez-barier/sluchove-znevyhodneni/organizace-spolky) | http://sk.olympia.sweb.cz/ | `http://sk.olympia.sweb.cz/` |
| [Organizace a spolky](https://www.mlp.cz/cz/o-knihovne/sluzby/knihovna-bez-barier/sluchove-znevyhodneni/organizace-spolky) | www.tamtam-praha.cz/index.php | `http://www.tamtam-praha.cz/index.php` |
| [Organizace a spolky](https://www.mlp.cz/cz/o-knihovne/sluzby/knihovna-bez-barier/zrakove-znevyhodneni/organizace-spolky) | http://szp.diakoniecce.cz/ | `http://szp.diakoniecce.cz/` |
| [Organizace a spolky](https://www.mlp.cz/cz/o-knihovne/sluzby/knihovna-bez-barier/zrakove-znevyhodneni/organizace-spolky) | http://divadloverva.cz/ | `http://divadloverva.cz/` |
| [Doporučujeme na internetu](https://www.mlp.cz/cz/o-knihovne/sluzby/specializovana-oddeleni/divadelni-filmove-oddeleni/doporucujeme-na-internetu) | www.imdb.cz | `http://www.imdb.cz` |
| [Doporučujeme na internetu](https://www.mlp.cz/cz/o-knihovne/sluzby/specializovana-oddeleni/divadelni-filmove-oddeleni/doporucujeme-na-internetu) | http://web.nfa.cz/…h/index.html | `http://web.nfa.cz/CeskyHranyFilm/cz/obsah/index.html` |
| [Doporučujeme na internetu](https://www.mlp.cz/cz/o-knihovne/sluzby/specializovana-oddeleni/hudebni-oddeleni/doporucujeme-na-internetu) | http://mus.jib.cz/ | `http://mus.jib.cz/` |
| [Doporučujeme na internetu](https://www.mlp.cz/cz/o-knihovne/sluzby/specializovana-oddeleni/hudebni-oddeleni/doporucujeme-na-internetu) | www.rozhlas.cz/d-dur/portal/ | `http://www.rozhlas.cz/d-dur/portal/` |
| [Doporučujeme na internetu](https://www.mlp.cz/cz/o-knihovne/sluzby/specializovana-oddeleni/hudebni-oddeleni/doporucujeme-na-internetu) | http://koncertyvpraze.cz/ | `http://koncertyvpraze.cz/` |
| [Doporučujeme na internetu](https://www.mlp.cz/cz/o-knihovne/sluzby/specializovana-oddeleni/hudebni-oddeleni/doporucujeme-na-internetu) | http://www.cenyandel.cz/ | `http://www.cenyandel.cz/` |
| [Doporučujeme na internetu](https://www.mlp.cz/cz/o-knihovne/sluzby/specializovana-oddeleni/hudebni-oddeleni/doporucujeme-na-internetu) | http://hudebnirozhledy.scena.cz/www/index.php | `http://hudebnirozhledy.scena.cz/www/index.php` |
| [Hudební e-zdroje](https://www.mlp.cz/cz/o-knihovne/sluzby/specializovana-oddeleni/hudebni-oddeleni/hudebni-e-zdroje) | Vstup do databáze | `https://shibboleth2sp.sams.oup.com/Shibboleth.sso/Login?entityID=https://gryf.mlp.cz/idp/shibboleth&target=ht…` |

<a id="external-http"></a>

## Cizí web bez https – ověřit ručně (17)

Priorita 3. Cizí web nemá zabezpečené https a přes http ho nešlo ověřit. Ověřte v prohlížeči.

| Kde | Text odkazu | Chybný odkaz |
|---|---|---|
| [Malešice](https://www.mlp.cz/cz/pobocky/malesice)<br>[Malešice](https://www.mlp.cz/en/pobocky/malesice) | Bytového domu Malešice | `http://www.bdmalesice.cz/` |
| [Foodblogerka Vilemína](https://www.mlp.cz/cz/akce/foodblogerka-vilemina/12234) | http://www.vilemininozatisi.cz/ | `http://www.vilemininozatisi.cz/` |
| [Semínkovna na Cibulce](https://www.mlp.cz/cz/novinky/seminkovna-na-cibulce) | www.seminkovny.com | `http://www.seminkovny.com/` |
| [Organizace a spolky](https://www.mlp.cz/cz/o-knihovne/sluzby/knihovna-bez-barier/mentalne-znevyhodneni/organizace-spolky) | http://www.praha.apla.cz/ | `http://www.praha.apla.cz/` |
| [Organizace a spolky](https://www.mlp.cz/cz/o-knihovne/sluzby/knihovna-bez-barier/mentalne-znevyhodneni/organizace-spolky) | http://www.dicre.ic.cz/ | `http://www.dicre.ic.cz/` |
| [Organizace a spolky](https://www.mlp.cz/cz/o-knihovne/sluzby/knihovna-bez-barier/mentalne-znevyhodneni/organizace-spolky) | http://strom.kbx.cz/ | `http://strom.kbx.cz/` |
| [Organizace a spolky](https://www.mlp.cz/cz/o-knihovne/sluzby/knihovna-bez-barier/mentalne-znevyhodneni/organizace-spolky) | http://www.ratolest.wz.cz/ | `http://www.ratolest.wz.cz/` |
| [Organizace a spolky](https://www.mlp.cz/cz/o-knihovne/sluzby/knihovna-bez-barier/sluchove-znevyhodneni/organizace-spolky) | www.amkn-cz.estranky.cz/ | `http://www.amkn-cz.estranky.cz/` |
| [Organizace a spolky](https://www.mlp.cz/cz/o-knihovne/sluzby/knihovna-bez-barier/sluchove-znevyhodneni/organizace-spolky) | www.frpsp.cz/cs-CZ/uvod.html | `http://www.frpsp.cz/cs-CZ/uvod.html` |
| [Organizace a spolky](https://www.mlp.cz/cz/o-knihovne/sluzby/knihovna-bez-barier/sluchove-znevyhodneni/organizace-spolky) | www.ipsknpraha.estranky.cz/ | `http://www.ipsknpraha.estranky.cz/` |
| [Organizace a spolky](https://www.mlp.cz/cz/o-knihovne/sluzby/knihovna-bez-barier/zrakove-znevyhodneni/organizace-spolky) | www.asociacerodicu.estranky.cz/ | `http://www.asociacerodicu.estranky.cz/` |
| [Doporučujeme na internetu](https://www.mlp.cz/cz/o-knihovne/sluzby/specializovana-oddeleni/divadelni-filmove-oddeleni/doporucujeme-na-internetu) | http://db.divadelni-ustav.cz/default.aspx | `http://db.divadelni-ustav.cz/default.aspx` |
| [Doporučujeme na internetu](https://www.mlp.cz/cz/o-knihovne/sluzby/specializovana-oddeleni/hudebni-oddeleni/doporucujeme-na-internetu) | http://www.jmw.cz/ | `http://www.jmw.cz/` |
| [Doporučujeme na internetu](https://www.mlp.cz/cz/o-knihovne/sluzby/specializovana-oddeleni/hudebni-oddeleni/doporucujeme-na-internetu) | Hudební katalog skladeb s notovými incipity ve správě NK ČR | `http://katif.nkp.cz/KatalogyHudba.aspx?katkey=061KHI` |
| [Doporučujeme na internetu](https://www.mlp.cz/cz/o-knihovne/sluzby/specializovana-oddeleni/hudebni-oddeleni/doporucujeme-na-internetu) | http://classicfm.lidovky.cz/ | `http://classicfm.lidovky.cz/` |
| [Doporučujeme na internetu](https://www.mlp.cz/cz/o-knihovne/sluzby/specializovana-oddeleni/hudebni-oddeleni/doporucujeme-na-internetu) | http://www.obecni-dum.cz/ | `http://www.obecni-dum.cz/` |
| [Doporučujeme na internetu](https://www.mlp.cz/cz/o-knihovne/sluzby/specializovana-oddeleni/hudebni-oddeleni/doporucujeme-na-internetu) | http://www.pkf.cz/ | `http://www.pkf.cz/` |

<a id="listing-empty"></a>

## Odkaz na prázdný výpis akcí (2)

Priorita 3. Odkaz vede na výpis akcí, který je teď prázdný a návštěvník vidí jen nadpis „Akce“. **Oprava pro správce webu:** doplnit do pohledu „Akce“ text pro prázdný výsledek (např. „Momentálně neprobíhá žádná výstava“).

| Kde | Text odkazu | Chybný odkaz |
|---|---|---|
| [Knihovna na veletrzích i jako hostitel festivalů](https://www.mlp.cz/cz/novinky/knihovna-na-veletrzich-i-jako-hostitel-festivalu) | Projekce v Ústřední knihovně | `https://www.mlp.cz/akce/vsechny-akce?field_event_type_target_id=11&nid_entityreference_filter=571&field_event…` |
| [Artotéka](https://www.mlp.cz/cz/o-knihovne/sluzby/specializovana-oddeleni/artoteka) | Aktuální výstava | `https://www.mlp.cz/cz/akce?field_event_type_target_id=21&nid_entityreference_filter=549&field_event_instance_…` |

## Jak kontrola proběhla

- Kontrolu jsem připravil a spustil s pomocí AI asistenta Claude (Anthropic): napsal skripty, které jsou v tomto repozitáři, a výsledky roztřídil. Vybrané nálezy byly ověřeny i v běžném prohlížeči.
- Prošli jsme všechny stránky ze sitemapy (`/default/sitemap.xml`) a ověřili každý odkaz a obrázek na nich. Stránky katalogu jsme samostatně neprocházeli.
- Server mlp.cz jsme zatěžovali nejvýše jedním požadavkem za sekundu podle `robots.txt`.
- Odkazy v hlavičce a patičce (stejné na všech stránkách) uvádíme jen jednou.
- Facebook, Instagram, YouTube a další weby automatické kontroly blokují; ty mezi chyby nepočítáme.
- Cizí weby, které se nenačetly, jsme zkoušeli třikrát; i tak mohou být jen dočasně nedostupné (proto priorita 3).
- Navržené opravy s označením „ověřeno“ fungují. U ostatních ověřte, že vedou na správnou stránku.
- Kontrolu lze zopakovat skripty v repozitáři (postup je v souboru [`README.md`](README.md)).
