/* Para crear una simulación de la difusión de un gas,tomamos la segunda ley
de Fick que describe el movimiento de sus partículas, de la siguiente forma:
                                ∂u/∂t = D*∇^2(u)
donde u es la función concentración que queremos hallar, ∇^2 es su Laplaciando
y D es el coeficiente de difusión del gas, en este caso constante.
Vemos entonces que la función concentración u depende tanto de las coordenadas
espaciales, como del tiempo. Entonces, si tomamos un espacio cartesiano,
podemos reescribir esto como:
            ∂u/∂t = D *[∂^2(u)/∂x^2 + ∂^2(u)/∂y^2 + ∂^2(u)/∂z^2]
con u = u(x,y,z,t) */

#include <fstream>
#include <iostream>
#include <math.h>
#include <stdio.h>
#include <time.h>
using namespace std;

const double l = 100;
const int n = 100;
const double dl = l/n;
const double dt = 0.25 * pow(dl,2);
const int instantes = 500;
const double tmin = 0;                /* Valores y condiciones iniciales */
const double tmax = instantes/dt;
const double D =  0.2;

int main(){

  double t[instantes] = { 0 };          /* el array de instantes en los que se evalúa la ecuación */
  for (int i = 1; i < instantes; i++){
    t[i] = t[i-1] + dt;
  }

  double u_pasado[n][n];              /* el array de condiciones iniciales */
  for (int i = 0; i < n; i++){
    for (int j = 0; j < n; j++){
      u_pasado[i][j] = 0;
    }
    u_pasado[0][i] = 1000;
  }
  /*srand(time(0));
  for (int i = 0; i < 20; i++){
    int a = rand() % 100;
    int b = rand() % 100;
    u_pasado[a][b] = 1000;
  }*/

  double u_presente[n][n] = {0};
  ofstream outfile;
  outfile.open("difusion_gas.csv");
  for (int k = 0; k < instantes; k++){

    for (int i = 1; i < n-1; i++){
      for (int j = 1; j < n-1; j++){
        u_presente[i][j] = u_pasado[i][j] + D*dt/pow(dl,2) * (u_pasado[i+1][j] - 4*u_pasado[i][j] + u_pasado[i-1][j] + u_pasado[i][j+1] + u_pasado[i][j-1]);
      }
    }

    for (int i = 1; i < n-1; i++){
      for (int j = 1; j < n-1; j++){
        u_pasado[i][j] = u_presente[i][j];
      }
    }


    for (int i = 0; i < n; i++){
      for (int j = 0; j < n; j++){
        outfile << u_presente[i][j] << ",";
      }
      outfile << endl;              /* se crea un archivo con los datos */
    }

  }
  outfile.close();

  return 0;
}
