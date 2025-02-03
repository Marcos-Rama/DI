package com.example.warframes.views;


import android.content.Intent;
import android.content.SharedPreferences;
import android.os.Bundle;
import android.util.Log;
import android.view.View;
import android.widget.Button;
import android.widget.Toast;

import androidx.appcompat.app.AppCompatActivity;
import androidx.appcompat.app.AppCompatDelegate;
import androidx.databinding.DataBindingUtil;
import androidx.lifecycle.ViewModelProvider;

import com.bumptech.glide.Glide;
import com.example.warframes.R;
import com.example.warframes.databinding.ActivityDetailBinding;
import com.example.warframes.viewmodels.DetailViewModel;


public class DetailActivity extends AppCompatActivity {
    private ActivityDetailBinding binding;
    private DetailViewModel viewModel;
    private String warframeName;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        SharedPreferences preferences = getSharedPreferences("settings", MODE_PRIVATE);
        boolean isDarkMode = preferences.getBoolean("dark_mode", false);

        // Aplicar el tema según la preferencia
        if (isDarkMode) {
            AppCompatDelegate.setDefaultNightMode(AppCompatDelegate.MODE_NIGHT_YES);
        } else {
            AppCompatDelegate.setDefaultNightMode(AppCompatDelegate.MODE_NIGHT_NO);
        }
        //Configura el binding para la vista
        binding = DataBindingUtil.setContentView(this, R.layout.activity_detail);

        viewModel = new ViewModelProvider(this).get(DetailViewModel.class);


        warframeName = getIntent().getStringExtra("name");
        Log.d("DetailActivity", "warframeId obtenido del Intent: " + warframeName);
        if (warframeName != null) {
            viewModel.checkIsFavorite(warframeName);
        } else {
            Log.e("DetailActivity", "warframeId es null al recibir el Intent");
        }

        //Extra los datos del intent
        String name = getIntent().getStringExtra("name");
        String description = getIntent().getStringExtra("description");
        String url = getIntent().getStringExtra("url");

        //Valida que los datos necesarios no estén vacíos
        if (name == null || description == null || url == null) {
            Toast.makeText(this, "Error al cargar los datos", Toast.LENGTH_SHORT).show();
            finish();
            return;
        }

        //Establece-vincula los datos en los elementos de la vista
        binding.titleTextView.setText(name);
        binding.descriptionTextView.setText(description);
        Glide.with(this).load(url).into(binding.imageView);

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

        setupFavoriteButton();

    }

    private void setupFavoriteButton() {
        viewModel.getIsFavorite().observe(this, isFavorite -> {
            if (isFavorite != null) {
                if (isFavorite) {
                    binding.favFavorite.setImageResource(R.drawable.si_fav); // Corazón favorito
                } else {
                    binding.favFavorite.setImageResource(R.drawable.no_fav); // Corazón NO favorito
                }
            }
        });
        binding.favFavorite.setOnClickListener(v -> {
            String warframeName = getIntent().getStringExtra("name");
            if (warframeName != null) {
                Log.d("DetailActivity", "Botón de favoritos pulsado, Warframe Name: " + warframeName);
                // Llamada a toggleFavorite en ViewModel con el name
                viewModel.toggleFavorite(warframeName);
            } else {
                Log.e("DetailActivity", "warframeName es null al hacer clic en favoritos");
            }
        });
    }
}