import logging
import sys
import collections
import fiona
from fiona.transform import transform_geom

logging.basicConfig(stream=sys.stderr, level=logging.INFO)
with fiona.open('shp/countries.shp', 'r') as source:
    # Copy the source schema and add two new properties.
    sink_schema = source.schema.copy()

    # Open to write complete GeoJSON
    with fiona.open(
                'countries.geojson', 'w',
                crs=source.crs,
                driver="GeoJSON",
                schema=sink_schema,
                ) as sink_all:

        dict_description = collections.OrderedDict()
        # Loop on each country feature
        for f in source:
            try:

                # The sink file is written to disk and closed when its block ends.
                sink_all.write(f)

                # Some "countries" do not have iso codes in Natural Earth
                # We use sov_a3 in this 3 special cases
                # CYN (Northern Cyprus), KOS (Kosovo), SOL (Somaliland)
                iso_a3 = f['properties']['iso_a3']
                if iso_a3 == '-99':
                    iso_a3 = f['properties']['sov_a3']
                iso_a3 = iso_a3.lower()
                dict_description[iso_a3] = f['properties']['formal_en']
                # Create a sink for processed features with the same format and
                # coordinate reference system as the source.
                with fiona.open(
                        'shp/' + iso_a3 + '.shp', 'w',
                        crs=source.crs,
                        driver=source.driver,
                        schema=sink_schema,
                        ) as sink:
                    # The sink file is written to disk and closed when its block ends.
                    sink.write(f)

                # Repeat the same operation but write to GeoJSON
                with fiona.open(
                        iso_a3 + '.geojson', 'w',
                        crs=source.crs,
                        driver="GeoJSON",
                        schema=sink_schema,
                        ) as sink:
                    # The sink file is written to disk and closed when its block ends.
                    sink.write(f)

            except Exception, e:
                logging.exception("Error processing feature %s:", f['id'])

description_readme = '''Geodata data package providing geojson polygons for all the world's countries.
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

{}

The `data` directory contains also a `shp` folder and the folder name is already a hint.

The Shapefile (also written SHP) is a "de-facto" standard for the geospatial industry.

Speaking about SHP, it's in fact a shortcut because SHP require more than one file to work correctly.
You will have `countries.shp`, `countries.dbf`, `countries.shx` and `countries.prj`. Moreover, we also kept original html description and history in the file `countries.README.html` and a `countries.VERSION.txt` to keep track of the original dataset changes.

To finish, like for GeoJSON, a SHP for each country following the same naming conventions is available.
'''

print description_readme.format('\n'.join(['* %s : %s' % (key, value) for (key, value) in sorted(dict_description.items())]))
