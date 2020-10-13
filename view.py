###TODO: Añadir listas canciones a cada stack asc y desc
###TODO: Etiquetas de ejemplo de notas en cada stack meterlas en una caja vertical y esa caja en la caja vertical del stack, en vez de meter directamente las etiquetas en la caja vertical del stack
###TODO: Añadir todos los intervalos al desplegable. Creo que faltan algunos
###TODO: Añadir funcionalidad al desplegable, que se cambien los datos según la opción seleccionada
###TODO: Cambiar fuente y ponerlo bonito, si se puede claro.

import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

import requests

intervalos = [["Selecciona intervalo"], ["Segunda menor"], ["Segunda mayor"], ["Tercera menor"], ["Tercera mayor"], ["Cuarta justa"], ["Cuarta aumentada"], ["Quinta justa"], ["Sexta menor"], ["Sexta mayor"], ["Séptima menor"], ["Séptima mayor"], ["Octava"]]

class View:
	def __init__(self):
		w=Gtk.Window(title="Intervalo Musical")
		w.connect("delete-event", Gtk.main_quit)

		#self.set_border_width(10)
		#self.set_default_size(300, 250)

		###Caja vertical principal
		vbox=Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=6)

		###Lista intervalos desplegable
		
		
		name_store = Gtk.ListStore(str)
		for i in range(len(intervalos)):#quitar este bucle y ponerlo como al ppo porque los bucles son muy ineficientes en python. Lo cambié a esto porque lo necesitaba para hacer una comprobación
			name_store.append(intervalos[i])
		###Horizontal box que guarda Intervalo con desplegable para seleccionar
		hbox = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=50)
		label = Gtk.Label(xalign=0)
		label.set_markup("<big>Intervalo</big>")
		#label1=Gtk.Label()
		#label1.show()
		self.name_combo = Gtk.ComboBox(model=name_store)
		cell = Gtk.CellRendererText()
		self.name_combo.pack_start(cell, False)
		self.name_combo.add_attribute(cell, "text", 0)
		self.name_combo.set_active(0)


		#button = Gtk.Button(label="Contar")#
		#button.show()#
		#self.name_combo.set_entry_text_column(1)
		#name_combo.connect("changed", self.on_combo_changed)

		hbox.pack_start(label, True, True, 0)
		hbox.pack_start(self.name_combo, False, True, 0)
		#hbox.pack_start(button, False, False, 8)#
		###Añade la linea del desplegable a la caja vertical principal
		vbox.add(hbox)

		###Separador (para que luzca bien)
		separator=Gtk.Separator(orientation=Gtk.Orientation.HORIZONTAL)
		separator.set_margin_top(10)
		vbox.add(separator)


		###Stack para seleccionar entre Ascendiente y Descendiente
		stack = Gtk.Stack()
		###Tipo y duración de animación del stack
		stack.set_transition_type(Gtk.StackTransitionType.SLIDE_LEFT_RIGHT)
		stack.set_transition_duration(1000)

		##############################
		###INICIO STACK ASCENDIENTE###
		##############################
		vbox_asc=Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=6)

		###Etiquetas de ejemplo de notas en el intervalo
		hbox_notas = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=50)
		title_notas = Gtk.Label()
		title_notas.set_margin_top(10)
		title_notas.set_markup("<big>Ejemplo de notas</big>")
		hbox_notas.pack_start(title_notas,expand=True,fill=True,padding=8)
		vbox_asc.add(hbox_notas)
		hbox_ej_notas=Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=50)
		ej_notas=Gtk.Label(label="Do - Sol♯")
		hbox_ej_notas.pack_start(ej_notas,expand=True,fill=True,padding=8)
		vbox_asc.add(hbox_ej_notas)

		###Separador
		separator_asc=Gtk.Separator(orientation=Gtk.Orientation.HORIZONTAL)
		separator_asc.set_margin_top(10)
		vbox_asc.add(separator_asc)

		###############################
		##PONER AQUI LISTA CANCIONES###
		###############################

		###########################
		###FIN STACK ASCENDIENTE###
		###########################


		###Añade el stack ascendiente al botón
		stack.add_titled(vbox_asc, "asc", "Asc")


		###############################
		###INICIO STACK DESCENDIENTE###
		###############################

		vbox_desc=Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=6)

		###Etiquetas de ejemplo de notas en el intervalo
		hbox_notas = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=50)
		title_notas = Gtk.Label()
		title_notas.set_margin_top(10)
		title_notas.set_markup("<big>Ejemplo de notas</big>")
		hbox_notas.pack_start(title_notas,expand=True,fill=True,padding=8)
		vbox_desc.add(hbox_notas)
		hbox_ej_notas=Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=50)
		ej_notas=Gtk.Label(label="Do - Mi")
		hbox_ej_notas.pack_start(ej_notas,expand=True,fill=True,padding=8)
		vbox_desc.add(hbox_ej_notas)

		###Separador
		separator_desc=Gtk.Separator(orientation=Gtk.Orientation.HORIZONTAL)
		separator_desc.set_margin_top(10)
		vbox_desc.add(separator_desc)

		###############################
		##PONER AQUI LISTA CANCIONES###
		###############################

		############################
		###FIN STACK DESCENDIENTE###
		############################
		
		###Añade el stack descendiente al botón
		stack.add_titled(vbox_desc, "desc", "Desc")
		#stack.connect("changed", self.on_stack_changed)
		###últimas configuraciones del stack
		stack_switcher = Gtk.StackSwitcher()
		stack_switcher.set_halign(3)
		stack_switcher.set_stack(stack)
		vbox.pack_start(stack_switcher, True, True, 0)
		vbox.pack_start(stack, True, True, 0)

		#########################
    	###GESTIÓN DE REQUESTS###
    	#########################
		self.request_asc="" #variable que guarda la consulta que se va a lanzar al servidor
		self.request_desc="" #variable que guarda la consulta que se va a lanzar al servidor
		self.request_devuelto_asc="" #variable que guarda lo que devuelve el servidor
		self.request_devuelto_desc = "" #variable que guarda lo que devuelve el servidor



		w.add(vbox)
		w.show_all()
        
        
        ######################
        ###EJEMPLO CONTADOR###
        ######################
		#self.button = button
		#self.count_label=label1
		#self.update_count(count)
        	
	#def connect_contar_clicked(self, handler):
	#	self.button.connect('clicked', handler)
		
	#def update_count(self, count):
	#	veces = "1 vez" if count == 1 else f"{count} veces"
	#	self.count_label.set_label(f"Has pulsado {veces}")
		
		######################
        ###EJEMPLO CONTADOR###
        ######################
       
	def connect_interval_changed(self, handler): #método que avisa al controller cuando se cambia la opción del combobox
		self.name_combo.connect('changed', handler)
	
	#def on_combo_changed(self, combo):
	#	if combo.get_active() != 0:
	#	    print("Seleccionaste "+str(intervalos[combo.get_active()][0])+str(combo.get_active()))
	#	return True
	
	#def on_stack_changed(self, stack):
	#	print("Seleccionaste "+str(stack_switcher.get_visible_child()))
	#	return True
		
	def set_request_asc(self, req): #método que asocia la consulta a su variable
		#print(req)
		self.request_asc=req
		
	def set_request_desc(self, req): #método que asocia la consulta a su variable
		#print(req)
		self.request_desc=req

	def request(self): #simplemente printea las consultas, no sirve para nada más que orientarse mientras codificas
		print(self.request_asc)
		print(self.request_desc)
	#def set_combo(self, inter):
	#	combo.set_active(inter)
	def send_request(self): # se ocupa de realizar las consultas
		self.request_devuelto_asc=requests.get(self.request_asc)
		self.request_devuelto_desc=requests.get(self.request_desc)
		print(self.request_devuelto_asc.text)
		print(self.request_devuelto_desc.text)
	def get_combo(self): #devuelve una referencia de que opción está seleccionada en el combobox
		return self.name_combo.get_active()
	
def start():
	Gtk.main()
