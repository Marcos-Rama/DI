package com.example.mycatalog;

import android.os.Bundle;
import android.view.MenuItem;

import androidx.annotation.NonNull;
import androidx.appcompat.app.AppCompatActivity;

import androidx.fragment.app.Fragment;

import com.google.android.material.bottomnavigation.BottomNavigationView;


public class MainActivity extends AppCompatActivity {
//Actividad que se inicia de primero cuando se ejecuta la aplicación
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
//Establece que se verá en la primera pantalla
        setContentView(R.layout.activity_main);
        if(savedInstanceState == null) {
            getSupportFragmentManager()
                    .beginTransaction()
                    .replace(R.id.fragmentContainer, new AboutFragment())
                    .commit();
        }
        //Crea la barra inferior con las funcionalidades que se quieran asignar
        BottomNavigationView bar = findViewById(R.id.bottomNavigation);
        bar.setOnItemSelectedListener(item -> {
            Fragment myFragment = null;

                if (item.getItemId() == R.id.menu1) {
                    //Si se selecciona esta opción viaja al fragment CatalogFragment
                    myFragment = new CatalogFragment();
                    getSupportFragmentManager()
                            .beginTransaction()
                            .replace(R.id.fragmentContainer, myFragment).
                            commit();
                }
                if (item.getItemId() == R.id.menu2) {
                    //Si se selecciona esta opción viaja al fragment AboutFragment
                    myFragment = new AboutFragment();
                    getSupportFragmentManager().beginTransaction().replace(R.id.fragmentContainer, myFragment).commit();
                }

                return true;

        });

    }
}