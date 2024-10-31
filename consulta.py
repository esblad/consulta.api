import requests
import tkinter as tk
from tkinter import messagebox

# Función para consultar la API de USGS
def consultar_api():
    url = "https://earthquake.usgs.gov/fdsnws/event/1/query"
    params = {
        "format": "geojson",
        "starttime": starttime_entry.get(),
        "endtime": endtime_entry.get(),
        "minmagnitude": minmag_entry.get(),
        "minlatitude": minlat_entry.get(),
        "maxlatitude": maxlat_entry.get(),
        "minlongitude": minlon_entry.get(),
        "maxlongitude": maxlon_entry.get()
    }
    
    try:
        response = requests.get(url, params=params)
        response.raise_for_status()
        data = response.json()
        
        # Limpiar la lista de resultados
        result_list.delete(0, tk.END)
        
        for feature in data['features']:
            lugar = feature['properties']['place']
            magnitud = feature['properties']['mag']
            result_list.insert(tk.END, f"Lugar: {lugar}, Magnitud: {magnitud}")
    except requests.exceptions.RequestException as e:
        messagebox.showerror("Error", f"Error al consultar la API: {e}")

# Configuración de la interfaz gráfica
root = tk.Tk()
root.title("Consulta de Terremotos")

# Etiquetas y entradas para los parámetros de consulta
tk.Label(root, text="Fecha de inicio (YYYY-MM-DD):").grid(row=0, column=0)
starttime_entry = tk.Entry(root)
starttime_entry.grid(row=0, column=1)

tk.Label(root, text="Fecha de fin (YYYY-MM-DD):").grid(row=1, column=0)
endtime_entry = tk.Entry(root)
endtime_entry.grid(row=1, column=1)

tk.Label(root, text="Magnitud mínima:").grid(row=2, column=0)
minmag_entry = tk.Entry(root)
minmag_entry.grid(row=2, column=1)

# Filtros de coordenadas para la región
tk.Label(root, text="Mínimo Latitud:").grid(row=3, column=0)
minlat_entry = tk.Entry(root)
minlat_entry.grid(row=3, column=1)

tk.Label(root, text="Máximo Latitud:").grid(row=4, column=0)
maxlat_entry = tk.Entry(root)
maxlat_entry.grid(row=4, column=1)

tk.Label(root, text="Mínimo Longitud:").grid(row=5, column=0)
minlon_entry = tk.Entry(root)
minlon_entry.grid(row=5, column=1)

tk.Label(root, text="Máximo Longitud:").grid(row=6, column=0)
maxlon_entry = tk.Entry(root)
maxlon_entry.grid(row=6, column=1)

# Botón para realizar la consulta
consultar_button = tk.Button(root, text="Consultar", command=consultar_api)
consultar_button.grid(row=7, column=0, columnspan=2)

# Lista para mostrar los resultados
result_list = tk.Listbox(root, width=50, height=15)
result_list.grid(row=8, column=0, columnspan=2)

# Iniciar la aplicación
root.mainloop()