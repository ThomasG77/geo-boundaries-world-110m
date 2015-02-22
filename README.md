Geodata data package providing geojson polygons for all the world's countries.
Perfect for use in apps and visualizations.

Directly at root level, you will find:

* a `datapackage.json` file
* a `README.md`, an associate description for the datapackage
* a `generate_from_shapefile.sh` to automate dataset update

## `scripts` directory

It contains a python script to automate extraction of each countries and data conversion.
The script requires GDAL Python bindings, a geospatial tool to manipulate formats and datasets content.
It relies on `Fiona`, a Python module you can install with `pip install fiona`.

## `data` directory

It contains a set of files coming from [Natural Earth Data](http://www.naturalearthdata.com/downloads/110m-cultural-vectors/110m-admin-0-countries/) website.

The provided data are based on the GeoJSON, a text based format for geospatial mainly for the web, popular for it simplicity

You can find in the directory:

* the `countries.geojson` using the GeoJSON, 
* a list of GeoJSON files we created for each countries.

In this case, the adopted naming convention is to use the attribute `iso_a3` to name the file.

Some "countries" do not have iso codes in Natural Earth and we adopted the use of `sov_a3`
 in this 3 special cases: CYN (Northern Cyprus), KOS (Kosovo) and SOL (Somaliland).

You can find below correspondance between codes and formal names to help you.

* afg : Islamic State of Afghanistan
* ago : People's Republic of Angola
* alb : Republic of Albania
* are : United Arab Emirates
* arg : Argentine Republic
* arm : Republic of Armenia
* ata : None
* atf : Territory of the French Southern and Antarctic Lands
* aus : Commonwealth of Australia
* aut : Republic of Austria
* aze : Republic of Azerbaijan
* bdi : Republic of Burundi
* bel : Kingdom of Belgium
* ben : Republic of Benin
* bfa : Burkina Faso
* bgd : People's Republic of Bangladesh
* bgr : Republic of Bulgaria
* bhs : Commonwealth of the Bahamas
* bih : Bosnia and Herzegovina
* blr : Republic of Belarus
* blz : Belize
* bol : Plurinational State of Bolivia
* bra : Federative Republic of Brazil
* brn : Negara Brunei Darussalam
* btn : Kingdom of Bhutan
* bwa : Republic of Botswana
* caf : Central African Republic
* can : Canada
* che : Swiss Confederation
* chl : Republic of Chile
* chn : People's Republic of China
* civ : Republic of Ivory Coast
* cmr : Republic of Cameroon
* cod : Democratic Republic of the Congo
* cog : Republic of Congo
* col : Republic of Colombia
* cri : Republic of Costa Rica
* cub : Republic of Cuba
* cyn : Turkish Republic of Northern Cyprus
* cyp : Republic of Cyprus
* cze : Czech Republic
* deu : Federal Republic of Germany
* dji : Republic of Djibouti
* dnk : Kingdom of Denmark
* dom : Dominican Republic
* dza : People's Democratic Republic of Algeria
* ecu : Republic of Ecuador
* egy : Arab Republic of Egypt
* eri : State of Eritrea
* esh : Sahrawi Arab Democratic Republic
* esp : Kingdom of Spain
* est : Republic of Estonia
* eth : Federal Democratic Republic of Ethiopia
* fin : Republic of Finland
* fji : Republic of Fiji
* flk : Falkland Islands
* fra : French Republic
* gab : Gabonese Republic
* gbr : United Kingdom of Great Britain and Northern Ireland
* geo : Georgia
* gha : Republic of Ghana
* gin : Republic of Guinea
* gmb : Republic of the Gambia
* gnb : Republic of Guinea-Bissau
* gnq : Republic of Equatorial Guinea
* grc : Hellenic Republic
* grl : Greenland
* gtm : Republic of Guatemala
* guy : Co-operative Republic of Guyana
* hnd : Republic of Honduras
* hrv : Republic of Croatia
* hti : Republic of Haiti
* hun : Republic of Hungary
* idn : Republic of Indonesia
* ind : Republic of India
* irl : Ireland
* irn : Islamic Republic of Iran
* irq : Republic of Iraq
* isl : Republic of Iceland
* isr : State of Israel
* ita : Italian Republic
* jam : Jamaica
* jor : Hashemite Kingdom of Jordan
* jpn : Japan
* kaz : Republic of Kazakhstan
* ken : Republic of Kenya
* kgz : Kyrgyz Republic
* khm : Kingdom of Cambodia
* kor : Republic of Korea
* kos : Republic of Kosovo
* kwt : State of Kuwait
* lao : Lao People's Democratic Republic
* lbn : Lebanese Republic
* lbr : Republic of Liberia
* lby : Libya
* lka : Democratic Socialist Republic of Sri Lanka
* lso : Kingdom of Lesotho
* ltu : Republic of Lithuania
* lux : Grand Duchy of Luxembourg
* lva : Republic of Latvia
* mar : Kingdom of Morocco
* mda : Republic of Moldova
* mdg : Republic of Madagascar
* mex : United Mexican States
* mkd : Former Yugoslav Republic of Macedonia
* mli : Republic of Mali
* mmr : Republic of the Union of Myanmar
* mne : Montenegro
* mng : Mongolia
* moz : Republic of Mozambique
* mrt : Islamic Republic of Mauritania
* mwi : Republic of Malawi
* mys : Malaysia
* nam : Republic of Namibia
* ncl : New Caledonia
* ner : Republic of Niger
* nga : Federal Republic of Nigeria
* nic : Republic of Nicaragua
* nld : Kingdom of the Netherlands
* nor : Kingdom of Norway
* npl : Nepal
* nzl : New Zealand
* omn : Sultanate of Oman
* pak : Islamic Republic of Pakistan
* pan : Republic of Panama
* per : Republic of Peru
* phl : Republic of the Philippines
* png : Independent State of Papua New Guinea
* pol : Republic of Poland
* pri : Commonwealth of Puerto Rico
* prk : Democratic People's Republic of Korea
* prt : Portuguese Republic
* pry : Republic of Paraguay
* pse : West Bank and Gaza
* qat : State of Qatar
* rou : Romania
* rus : Russian Federation
* rwa : Republic of Rwanda
* sau : Kingdom of Saudi Arabia
* sdn : Republic of the Sudan
* sen : Republic of Senegal
* slb : None
* sle : Republic of Sierra Leone
* slv : Republic of El Salvador
* sol : Republic of Somaliland
* som : Federal Republic of Somalia
* srb : Republic of Serbia
* ssd : Republic of South Sudan
* sur : Republic of Suriname
* svk : Slovak Republic
* svn : Republic of Slovenia
* swe : Kingdom of Sweden
* swz : Kingdom of Swaziland
* syr : Syrian Arab Republic
* tcd : Republic of Chad
* tgo : Togolese Republic
* tha : Kingdom of Thailand
* tjk : Republic of Tajikistan
* tkm : Turkmenistan
* tls : Democratic Republic of Timor-Leste
* tto : Republic of Trinidad and Tobago
* tun : Republic of Tunisia
* tur : Republic of Turkey
* twn : None
* tza : United Republic of Tanzania
* uga : Republic of Uganda
* ukr : Ukraine
* ury : Oriental Republic of Uruguay
* usa : United States of America
* uzb : Republic of Uzbekistan
* ven : Bolivarian Republic of Venezuela
* vnm : Socialist Republic of Vietnam
* vut : Republic of Vanuatu
* yem : Republic of Yemen
* zaf : Republic of South Africa
* zmb : Republic of Zambia
* zwe : Republic of Zimbabwe

The `data` directory contains also a `shp` folder and the folder name is already a hint.

The Shapefile (also written SHP) is a "de-facto" standard for the geospatial industry.

Speaking about SHP in fact a shortcut because SHP require more than one file to work correctly.
You will have `countries.shp`, `countries.dbf`, `countries.shx` and `countries.prj`. Moreover, we also kept original html description and history in the file `countries.README.html` and a `countries.VERSION.txt` to keep track of the original dataset changes.

To finish, like for GeoJSON, a SHP for each country following the same naming conventions is available.

