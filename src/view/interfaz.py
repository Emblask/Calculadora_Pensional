from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.spinner import Spinner
from kivy.uix.scrollview import ScrollView
from kivy.uix.gridlayout import GridLayout
from kivy.uix.popup import Popup
from kivy.core.window import Window
from kivy.graphics import Color, Rectangle
from kivy.uix.anchorlayout import AnchorLayout
from kivy.metrics import dp
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

try:
    from model import pylogic
except ImportError:
    class PyLogicMock:
        def pension_total(self, *args, **kwargs):
            return 25000.0
    pylogic = PyLogicMock()

primary_color = [0.2, 0.6, 0.5, 1]  
light_bg_color = [0.95, 0.95, 0.95, 1]  
text_color = [0.2, 0.2, 0.2, 1]  
visible_text_color = [0.1, 0.1, 0.1, 1]  

class BorderedLabel(Label):
    def __init__(self, **kwargs):
        super(BorderedLabel, self).__init__(**kwargs)
        self.bold = True
        self.color = primary_color
        with self.canvas.before:
            Color(0.93, 0.93, 0.93, 1)
            self.rect = Rectangle(pos=(0, 0), size=(0, 0))  
        self.bind(pos=self._update_rect, size=self._update_rect)
        
    def _update_rect(self, instance, value):
        self.rect.pos = self.pos
        self.rect.size = self.size

class StyledButton(Button):
    def __init__(self, **kwargs):
        super(StyledButton, self).__init__(**kwargs)
        self.background_color = primary_color
        self.background_normal = ""
        self.color = [1, 1, 1, 1]
        self.bold = True
        self.font_size = '16sp'

class PensionApp(App):
    def build(self):
        # Configurar ventana
        Window.clearcolor = light_bg_color
        Window.size = (900, 700)
        
        # Layout principal
        main_layout = BoxLayout(orientation='vertical', padding=20, spacing=15)
        
        # Header con título
        header = BoxLayout(orientation='horizontal', size_hint_y=0.12, spacing=10)
        
        # Título principal
        title_label = Label(
            text="CALCULADORA DE PENSIÓN",
            font_size='24sp',
            bold=True,
            color=primary_color
        )
        header.add_widget(title_label)
        main_layout.add_widget(header)
        
        # Contenido principal
        content = BoxLayout(orientation='horizontal', size_hint_y=0.88, spacing=20)
        
        # Panel izquierdo (formulario)
        left_panel = BoxLayout(orientation='vertical', size_hint_x=0.6, spacing=15)
        form_title = BorderedLabel(
            text="Ingrese sus datos personales para el cálculo",
            size_hint_y=0.08,
            font_size='18sp',
            padding=[15, 0]
        )
        left_panel.add_widget(form_title)
        
        scroll = ScrollView()
        form_grid = GridLayout(cols=2, spacing=15, size_hint_y=None, padding=[10, 10])
        form_grid.bind(minimum_height=form_grid.setter('height'))
        
        label_height = dp(40)
        input_height = dp(40)
        
        form_grid.add_widget(Label(
        ))
        self.edad_input = TextInput(
            multiline=False, 
            input_filter='int',
            size_hint_y=None, 
            height=input_height,
            background_color=[0.95, 0.95, 0.95, 1],
            padding=[10, 10, 0, 0],
            hint_text="Ingrese su edad"
        )
        form_grid.add_widget(self.edad_input)
        
        form_grid.add_widget(Label(
        ))
        self.genero_spinner = Spinner(
            text='Seleccione su género',
            values=('Masculino', 'Femenino'),
            size_hint_y=None,
            height=input_height,
            background_color=[0.95, 0.95, 0.95, 1]
        )
        form_grid.add_widget(self.genero_spinner)
        
        form_grid.add_widget(Label(
        ))
        self.semanas_input = TextInput(
            multiline=False, 
            input_filter='int',
            size_hint_y=None, 
            height=input_height,
            background_color=[0.95, 0.95, 0.95, 1],
            padding=[10, 10, 0, 0],
            hint_text="Número de semanas"
        )
        form_grid.add_widget(self.semanas_input)
        
        form_grid.add_widget(Label(
        ))
        self.hijos_input = TextInput(
            multiline=False, 
            input_filter='int',
            size_hint_y=None, 
            height=input_height,
            background_color=[0.95, 0.95, 0.95, 1],
            padding=[10, 10, 0, 0],
            hint_text="Número de hijos"
        )
        form_grid.add_widget(self.hijos_input)
        
        # Salarios con título separado
        salarios_title = BorderedLabel(
            text="Historial de Salarios",
            size_hint_y=None,
            height=label_height,
            font_size='16sp',
            halign='center'
        )
        form_grid.add_widget(salarios_title)
        form_grid.add_widget(Label(size_hint_y=None, height=label_height))  
        
        self.salarios_inputs = []
        for i in range(10):
            form_grid.add_widget(Label(
            ))
            salario_input = TextInput(
                multiline=False, 
                input_filter='int',
                size_hint_y=None, 
                height=input_height,
                background_color=[0.95, 0.95, 0.95, 1],
                padding=[10, 10, 0, 0],
                hint_text=f"Ingrese salario del año {i+1}"
            )
            self.salarios_inputs.append(salario_input)
            form_grid.add_widget(salario_input)
        
        scroll.add_widget(form_grid)
        left_panel.add_widget(scroll)
        
        # Botón de cálculo 
        button_layout = AnchorLayout(anchor_x='center', size_hint_y=0.1)
        self.calcular_btn = StyledButton(
            text="CALCULAR MI PENSIÓN", 
            size_hint=(0.7, 1)
        )
        self.calcular_btn.bind(on_press=self.calcular_pension)
        button_layout.add_widget(self.calcular_btn)
        left_panel.add_widget(button_layout)
        
        # Panel derecho (información)
        right_panel = BoxLayout(orientation='vertical', size_hint_x=0.4, spacing=15)
        
        # Instrucciones
        instructions_box = BoxLayout(orientation='vertical', size_hint_y=0.3)
        with instructions_box.canvas.before:
            Color(*primary_color)
            self.instructions_rect = Rectangle(pos=(0, 0), size=(0, 0))
        instructions_box.bind(pos=self._update_rect_pos_size, size=self._update_rect_pos_size)
        
        instructions_title = Label(
            text="INSTRUCCIONES", 
            font_size='18sp', 
            bold=True, 
            color=[1,1,1,1],
            size_hint_y=0.3
        )
        instructions_text = Label(
        text="Complete todos los campos del formulario con sus datos personales y su historial salarial de los últimos 10 años para obtener un cálculo estimado de su pensión.",
        color=[1, 1, 1, 1],
        font_size='16sp',
        halign='center',
        valign='middle',
        size_hint=(1, 1),
        text_size=(0, None)  # Importante para forzar el re-wrap dinámico
        )

        instructions_box.add_widget(instructions_title)
        instructions_box.add_widget(instructions_text)
        right_panel.add_widget(instructions_box)
        instructions_text.bind(size=lambda instance, value: setattr(instance, 'text_size', (instance.width - 40, None)))
        # Cómo funciona (con ajustes para visibilidad)
        como_funciona_box = BoxLayout(orientation='vertical', size_hint_y=0.6, spacing=5)
        
        title_container = BoxLayout(orientation='vertical', size_hint_y=0.15)
        with title_container.canvas.before:
            Color(0.93, 0.93, 0.93, 1)  # Color gris claro para el fondo
            self.title_rect = Rectangle(pos=(0, 0), size=(0, 0))
        title_container.bind(pos=self._update_title_rect, size=self._update_title_rect)
        
        como_funciona_title = Label(
            text="Cómo Funciona",
            font_size='18sp',
            bold=True,
            color=primary_color,
            halign='center'
        )
        title_container.add_widget(como_funciona_title)
        como_funciona_box.add_widget(title_container)
        
        como_funciona_box.add_widget(BoxLayout(size_hint_y=0.05))
        
        steps_box = BoxLayout(orientation='vertical', spacing=20, size_hint_y=0.8, padding=[20, 10])
        
        steps = [
            "1. Complete el formulario con sus datos",
            "2. Ingrese sus salarios de los últimos 10 años",
            "3. Haga clic en CALCULAR"
        ]
        
        for step in steps:
            step_container = BoxLayout(orientation='horizontal', size_hint_y=None, height=dp(90))
            
            step_label = Label(
                text=step,
                halign='left',
                valign='middle',
                text_size=(300, dp(90)),  # Forzar wrap y alineación
                color=visible_text_color,  # Color oscuro para mayor visibilidad
                font_size='18sp',  # Tamaño adecuado
                bold=True,  # Negrita para destacar
                size_hint_x=1
            )
            step_container.add_widget(step_label)
            steps_box.add_widget(step_container)
        
        como_funciona_box.add_widget(steps_box)
        right_panel.add_widget(como_funciona_box)
        
        content.add_widget(left_panel)
        content.add_widget(right_panel)
        main_layout.add_widget(content)
        
        return main_layout
    
    def _update_rect_pos_size(self, instance, value):
        """Actualiza la posición y tamaño de un rectángulo asociado a una instancia"""
        if hasattr(self, 'instructions_rect'):
            self.instructions_rect.pos = instance.pos
            self.instructions_rect.size = instance.size
    
    def _update_title_rect(self, instance, value):
        """Actualiza la posición y tamaño del rectángulo del título"""
        if hasattr(self, 'title_rect'):
            self.title_rect.pos = instance.pos
            self.title_rect.size = instance.size
    
    def mostrar_popup(self, titulo, mensaje):
        layout = BoxLayout(orientation='vertical', padding=20, spacing=10)
        
        # Contenido del popup
        layout.add_widget(Label(
            text=mensaje,
            font_size='16sp',
            halign='center',
            color=[0.1, 0.1, 0.1, 1],
            size_hint_y=0.7
        ))
        
        # Botón para cerrar
        cerrar_btn = StyledButton(
            text="Cerrar resultado", 
            size_hint=(0.5, 0.3)
        )
        button_box = AnchorLayout(anchor_x='center')
        button_box.add_widget(cerrar_btn)
        layout.add_widget(button_box)
        
        # Crear y mostrar popup
        popup = Popup(
            title=titulo,
            content=layout,
            size_hint=(0.6, 0.4),
            title_color=primary_color,
            title_size='18sp',
            background="",
            background_color=[0.98, 0.98, 0.98, 1]
        )
        cerrar_btn.bind(on_press=popup.dismiss)
        popup.open()
    
    def calcular_pension(self, instance):
        try:
            # Validación de campos
            if not self.edad_input.text:
                self.mostrar_popup("Campo Requerido", "Por favor ingrese su edad.")
                return
                
            if not self.semanas_input.text:
                self.mostrar_popup("Campo Requerido", "Por favor ingrese las semanas cotizadas.")
                return
                
            if not self.hijos_input.text:
                self.mostrar_popup("Campo Requerido", "Por favor ingrese la cantidad de hijos.")
                return
                
            if self.genero_spinner.text == 'Seleccione su género':
                self.mostrar_popup("Campo Requerido", "Por favor seleccione su género.")
                return
            
            # Verificar que se ingresaron todos los salarios
            salarios_faltantes = [i+1 for i, s in enumerate(self.salarios_inputs) if not s.text]
            if salarios_faltantes:
                texto_faltantes = ", ".join(str(i) for i in salarios_faltantes)
                self.mostrar_popup("Campos Incompletos", f"Faltan los salarios de los años: {texto_faltantes}")
                return
            
            # Procesar datos
            edad = int(self.edad_input.text)
            genero = self.genero_spinner.text
            semanas = int(self.semanas_input.text)
            hijos = int(self.hijos_input.text)
            salarios = [int(s.text) for s in self.salarios_inputs]
            
            # Calcular pensión
            resultado = pylogic.pension_total(salarios, genero, edad, semanas, hijos)
            
            # Mostrar resultado formateado
            resultado_formateado = "${:,.2f}".format(resultado)
            self.mostrar_popup(
                "RESULTADO DE SU PENSIÓN", 
                f"De acuerdo a los datos proporcionados,\nsu pensión mensual estimada sería de:\n\n{resultado_formateado}"
            )
        except ValueError:
            self.mostrar_popup("Error de Formato", "Por favor verifique que todos los campos numéricos contengan solo números.")
        except Exception as e:
            self.mostrar_popup("Error", f"Se produjo un error inesperado: {str(e)}")

if __name__ == "__main__":
    PensionApp().run()
