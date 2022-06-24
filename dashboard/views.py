from multiprocessing import context
from django.shortcuts import render
import plotly.graph_objects as go
import numpy as np
import random

from .models import Dashboard
#Create figure

def obj_Mesh_conus(skv_x, skv_y, skv_z,skv_name):

    return go.Mesh3d(

    )

def obj_Mesh_cube(skv_x, skv_y, skv_z,skv_name):
        return go.Mesh3d(
            x=[skv_x, skv_x, skv_x-2,skv_x-2, skv_x, skv_x, skv_x-2,skv_x-2],
            y=[skv_y, skv_y+2, skv_y+2, skv_y, skv_y, skv_y+2, skv_y+2, skv_y],
            z=[0, 0, 0, 0 ,skv_z, skv_z, skv_z, skv_z],

            colorbar_title='z',
            colorscale=[[0, 'gold'],
                    [1, 'magenta']],

            # Intensity of each vertex, which will be interpolated and color-coded
            intensity = np.linspace(0, 1, 8, endpoint=True),
            # i, j and k give the vertices of triangles
            i = [7, 0, 0, 0, 4, 4, 6, 6, 4, 0, 3, 2],
            j = [3, 4, 1, 2, 5, 6, 5, 2, 0, 1, 6, 3],
            k = [0, 7, 2, 3, 6, 7, 1, 1, 5, 5, 7, 6],

            text=skv_name,

            name='y',
            showscale=True
        )

def index(request):

    data = Dashboard.objects.all()
    print(data)

    layout =go.Layout(
        title=f'Визуализация данных журнала ...',
        width=1600,
        height=900,
        # legend_bgcolor= '#000000'
    )
    # for item in data:
    #     figure = go.Figure(obj_Mesh_cube(item.skv_x, item.skv_y, item.skv_z, item.skv_name), layout=layout).to_html()

    figure = go.Figure([obj_Mesh_cube(item.skv_x, item.skv_y, item.skv_z, item.skv_name) for item in data], layout=layout ).to_html()


    # for item in data:
    #     figure.add_trace(obj_Mesh_cube(item.skv_x, item.skv_y, item.skv_z, item.skv_name)).to_html()


    # figure.update_traces().to_html()

    context = {
        'figure' : figure, 
        }
    return render(request, 'dashboard/index.html', context)