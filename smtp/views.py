from django.shortcuts import render
from django.views.generic import TemplateView
import folium
from folium import plugins

import ee

ee.Initialize()


class Home(TemplateView):
    template_name="index.html"

    def get_context_data(self, **kwargs):
        figure=folium.Figure()

        # create folium object
        m=folium.Map(
            location=[28.5973518,83.54495724],
            zoom_start=8
        )
        m.add_to(figure)
        
        # select dataset to modis the data
        dataset = (ee.ImageCollection('MODIS/006/MOD13Q1')
                  .filter(ee.Filter.date('2019-07-01', '2019-11-30'))
                  .first())
        modisndvi = dataset.select('NDVI')

        # styling
        vis_paramsNDVI = {
            'min': 0,
            'max': 9000,
            'palette': [ 'FE8374', 'C0E5DE', '3A837C','034B48',]}

        # add map to the folium app
        map_id_dict = ee.Image(modisndvi).getMapId(vis_paramsNDVI)

        #GEE raster data to TileLayer
        folium.raster_layers.TileLayer(
                    tiles = map_id_dict['tile_fetcher'].url_format,
                    attr = 'Google Earth Engine',
                    name = 'NDVI',
                    overlay = True,
                    control = True
                    ).add_to(m)

        
        #add Layer control
        m.add_child(folium.LayerControl())
       
        #figure 
        figure.render()
         
        #return map
        return {"map": figure}
