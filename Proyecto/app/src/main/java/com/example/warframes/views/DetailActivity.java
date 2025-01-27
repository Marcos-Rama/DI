package com.example.warframes.views;


import android.content.Intent;
import android.os.Bundle;
import android.util.Log;
import android.view.View;
import android.widget.Button;
import android.widget.Toast;

import androidx.appcompat.app.AppCompatActivity;
import androidx.databinding.DataBindingUtil;

import com.bumptech.glide.Glide;
import com.example.warframes.R;
import com.example.warframes.databinding.ActivityDetailBinding;


public class DetailActivity extends AppCompatActivity {
    private static final String TAG = "DetailActivity";
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        //Para comprobar fallos que puedan dar, no es necesario para la funcionalidad
        Bundle extras = getIntent().getExtras();
        if (extras != null) {
            Log.d("DetailActivity", "Name: " + extras.getString("name"));
            Log.d("DetailActivity", "Description: " + extras.getString("description"));
            Log.d("DetailActivity", "URL: " + extras.getString("url"));
        } else {
            Log.e("DetailActivity", "No extras found in intent");
        }

        //Configura el binding para la vista
        ActivityDetailBinding binding = DataBindingUtil.setContentView(this, R.layout.activity_detail);

        //Extra los datos del intent
        String name = getIntent().getStringExtra("name");
        String description = getIntent().getStringExtra("description");
        String url = getIntent().getStringExtra("url");

        //Valida que los datos necesarios no estén vacíos
        if (name == null || description == null || url == null) {
            Log.e(TAG, "Datos incompletos del Warframe");
            Toast.makeText(this, "Error al cargar los datos", Toast.LENGTH_SHORT).show();
            finish();
            return;
        }
        //Establece-vincula los datos en los elementos de la vista
        binding.titleTextView.setText(name);
        binding.descriptionTextView.setText(description);
        Glide.with(this).load(url).into(binding.imageView); //Glide necesario para mostrar una imagen

        //Configuración de la función del botón de Logout
        Button logOutButton = findViewById(R.id.logOutButton);
        logOutButton.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {

                Intent loginIntent = new Intent(DetailActivity.this, LoginActivity.class);
                startActivity(loginIntent);
                finish();
            }
        });
    }
}