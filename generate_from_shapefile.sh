wget http://www.naturalearthdata.com/http//www.naturalearthdata.com/download/110m/cultural/ne_110m_admin_0_countries.zip
unzip ne_110m_admin_0_countries.zip
rm ne_110m_admin_0_countries.zip
rename -f "s/ne_110m_admin_0_countries/countries/g" *
mv countries.* data/shp/
cd data && python ../scripts/extract_features_from_countries.py > ../README.md
cd ..
