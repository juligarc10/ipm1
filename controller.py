import model
import view

class Controller:
	def __init__(self):
		self.model = model.Model()#crea modelo
		self.view = view.View()#crea view
		#self.view.connect_contar_clicked(self.on_contar_clicked)
		self.view.connect_interval_changed(self.on_combo_changed) #comprueba si cambió la opción de combobox
		
	#def on_contar_clicked(self, widget):
	#	self.model.count_up()
	#	self.view.update_count(self.model.count)
	
	def on_combo_changed(self, widget):
		print(str(self.view.get_combo())) #imprime el numero que tiene asociado el intervalo seleccionado
		self.model.asocia_intervalo(self.view.get_combo())# se actualiza el intervalo en el model
		if self.view.get_combo()==1:
			self.view.set_request_asc("http://127.0.0.1:5000/songs/2m/asc") #se devuelve la consulta adecuada dependiendo de qué intervalo esté seleccionado
			self.view.set_request_desc("http://127.0.0.1:5000/songs/2m/des")
		elif self.view.get_combo()==2:
			self.view.set_request_asc("http://127.0.0.1:5000/songs/2M/asc")
			self.view.set_request_desc("http://127.0.0.1:5000/songs/2M/des")
		elif self.view.get_combo()==3:
			self.view.set_request_asc("http://127.0.0.1:5000/songs/3m/asc")
			self.view.set_request_desc("http://127.0.0.1:5000/songs/3m/des")
		elif self.view.get_combo()==4:
			self.view.set_request_asc("http://127.0.0.1:5000/songs/3M/asc")
			self.view.set_request_desc("http://127.0.0.1:5000/songs/3M/des")
		elif self.view.get_combo()==5:
			self.view.set_request_asc("http://127.0.0.1:5000/songs/4j/asc")
			self.view.set_request_desc("http://127.0.0.1:5000/songs/4j/des")
		elif self.view.get_combo()==6:
			self.view.set_request_asc("http://127.0.0.1:5000/songs/4aum/asc")
			self.view.set_request_desc("http://127.0.0.1:5000/songs/4aum/des")
		elif self.view.get_combo()==7:
			self.view.set_request_asc("http://127.0.0.1:5000/songs/5j/asc")
			self.view.set_request_desc("http://127.0.0.1:5000/songs/5j/des")
		elif self.view.get_combo()==8:
			self.view.set_request_asc("http://127.0.0.1:5000/songs/6m/asc")
			self.view.set_request_desc("http://127.0.0.1:5000/songs/6m/des")
		elif self.view.get_combo()==9:
			self.view.set_request_asc("http://127.0.0.1:5000/songs/6M/asc")
			self.view.set_request_desc("http://127.0.0.1:5000/songs/6M/des")
		elif self.view.get_combo()==10:
			self.view.set_request_asc("http://127.0.0.1:5000/songs/7m/asc")
			self.view.set_request_desc("http://127.0.0.1:5000/songs/7m/des")
		elif self.view.get_combo()==11:
			self.view.set_request_asc("http://127.0.0.1:5000/songs/7M/asc")
			self.view.set_request_desc("http://127.0.0.1:5000/songs/7M/des")
		elif self.view.get_combo()==12:
			self.view.set_request_asc("http://127.0.0.1:5000/songs/8j/asc")
			self.view.set_request_desc("http://127.0.0.1:5000/songs/8j/des")
		self.view.request() #imprime la consulta al servidor (esto es orientativo)
		self.view.send_request()#imprime la respuesta del servidor (esto es orientativo)
	def start(self):
		view.start()
