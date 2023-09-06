#include <iostream>
#include <string>
#include <gtkmm.h>

using namespace std;

class Calculadora : public Gtk::Window {
public:
  Calculadora() {
    // Creamos los widgets de la interfaz gráfica
    Gtk::Label *etiqueta1 = new Gtk::Label("Primer número:");
    Gtk::Entry *entrada1 = new Gtk::Entry();
    Gtk::Label *etiqueta2 = new Gtk::Label("Segundo número:");
    Gtk::Entry *entrada2 = new Gtk::Entry();
    Gtk::Button *botonSumar = new Gtk::Button("Sumar");
    Gtk::Button *botonRestar = new Gtk::Button("Restar");
    Gtk::Button *botonMultiplicar = new Gtk::Button("Multiplicar");
    Gtk::Button *botonDividir = new Gtk::Button("Dividir");
    Gtk::Label *etiquetaResultado = new Gtk::Label("Resultado:");
    Gtk::Label *resultado = new Gtk::Label();

    // Agregamos los widgets al contenedor de la ventana
    add(etiqueta1);
    add(entrada1);
    add(etiqueta2);
    add(entrada2);
    add(botonSumar);
    add(botonRestar);
    add(botonMultiplicar);
    add(botonDividir);
    add(etiquetaResultado);
    add(resultado);

    // Configuramos el tamaño de la ventana
    set_size_request(300, 200);

    // Agregamos los eventos a los botones
    botonSumar->signal_clicked().connect(sigc::mem_fun(*this, &Calculadora::on_boton_sumar_clicked));
    botonRestar->signal_clicked().connect(sigc::mem_fun(*this, &Calculadora::on_boton_restar_clicked));
    botonMultiplicar->signal_clicked().connect(sigc::mem_fun(*this, &Calculadora::on_boton_multiplicar_clicked));
    botonDividir->signal_clicked().connect(sigc::mem_fun(*this, &Calculadora::on_boton_dividir_clicked));

    // Mostramos la ventana
    show_all();
  }

private:
  void on_boton_sumar_clicked() {
    // Obtenemos los números ingresados por el usuario
    double numero1 = stod(entrada1->get_text());
    double numero2 = stod(entrada2->get_text());

    // Calculamos la suma
    double resultado = numero1 + numero2;

    // Mostramos el resultado
    this->resultado->set_text(to_string(resultado));
  }

  void on_boton_restar_clicked() {
    // Obtenemos los números ingresados por el usuario
    double numero1 = stod(entrada1->get_text());
    double numero2 = stod(entrada2->get_text());

    // Calculamos la resta
    double resultado = numero1 - numero2;

    // Mostramos el resultado
    this->resultado->set_text(to_string(resultado));
  }

  void on_boton_multiplicar_clicked() {
    // Obtenemos los números ingresados por el usuario
    double numero1 = stod(entrada1->get_text());
    double numero2 = stod(entrada2->get_text());

    // Calculamos la multiplicación
    double resultado = numero1 * numero2;

    // Mostramos el resultado
    this->resultado->set_text(to_string(resultado));
  }

  void on_boton_dividir_clicked() {
    // Obtenemos los números ingresados por el usuario
    double numero1 = stod(entrada1->get_text());
    double numero2 = stod(entrada2->get_text());

    // Calculamos la división
    double resultado = numero1 / numero2;

    // Mostramos el resultado
    this->resultado->set_text(to_string(resultado));
  }

