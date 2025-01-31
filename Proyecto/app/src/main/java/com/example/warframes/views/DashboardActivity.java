package com.example.warframes.views;

import android.content.Intent;
import android.content.SharedPreferences;
import android.os.Bundle;
import android.util.Log;
import android.view.View;
import android.widget.Button;
import android.content.Context;

import androidx.appcompat.app.AppCompatActivity;
import androidx.appcompat.app.AppCompatDelegate;
import androidx.databinding.DataBindingUtil;
import androidx.lifecycle.ViewModelProvider;
import androidx.recyclerview.widget.LinearLayoutManager;

import com.example.warframes.R;
import com.example.warframes.adapters.WarframeAdapter;
import com.example.warframes.databinding.ActivityDashboardBinding;
import com.example.warframes.utils.ThemeSharedPreferences;
import com.example.warframes.viewmodels.DashboardViewModel;

import java.util.ArrayList;

public class DashboardActivity extends AppCompatActivity {
    //ViewModel para los datos de warframes
    private DashboardViewModel warframeViewModel;
    //Adapter para el recycler
    private WarframeAdapter warframeAdapter;
    private Context context = this;
    private Button themeButton;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        //Aplicar el modo que esté establecido
        SharedPreferences preferences = getSharedPreferences("settings", MODE_PRIVATE);
        boolean isDarkMode = preferences.getBoolean("dark_mode", false);

        if (isDarkMode) {
            AppCompatDelegate.setDefaultNightMode(AppCompatDelegate.MODE_NIGHT_YES);
        } else {
            AppCompatDelegate.setDefaultNightMode(AppCompatDelegate.MODE_NIGHT_NO);
        }
        super.onCreate(savedInstanceState);
        //Configura el binding para la vista del dashboard
        ActivityDashboardBinding binding = DataBindingUtil.setContentView(this, R.layout.activity_dashboard);

        Button logOutButton = findViewById(R.id.logOutButtonMain);

        //Botón para modo oscuro/claro
        themeButton = findViewById(R.id.themeButton);
        updateThemeButtonText(isDarkMode);
        themeButton.setOnClickListener(v -> toggleTheme(themeButton));

        //Crea el adapter con un listener para poder hacer click
        warframeAdapter = new WarframeAdapter(new ArrayList<>(), warframe -> {
            Log.d("DashboardActivity", "warframeId: " + warframe.getId());
            //Crea un intent para la pantalla details (luego DetailActivity lo obtendrá de aqui)
            Intent intent = new Intent(this, DetailActivity.class);
            intent.putExtra("id", warframe.getId());
            intent.putExtra("name", warframe.getName());
            intent.putExtra("description", warframe.getDescription());
            intent.putExtra("url", warframe.getUrl());
            startActivity(intent);
        });

        //Configura el recycler con un LinearLayaout y el adapter
        binding.recyclerView.setLayoutManager(new LinearLayoutManager(this));
        binding.recyclerView.setAdapter(warframeAdapter);

        warframeViewModel = new ViewModelProvider(this).get(DashboardViewModel.class);

        //Observa los cambios en la lista de warframes
        warframeViewModel.getWarframeLiveData().observe(this, warframes -> warframeAdapter.setWarframe(warframes));

        //Manejo del cierre de sesión
        logOutButton.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                Intent myIntent = new Intent(context, LoginActivity.class);
                context.startActivity(myIntent);
            }
        });
        binding.toFavorites.setOnClickListener(v -> {
            Intent intent = new Intent(this, FavoritesActivity.class);
            startActivity(intent);
        });


    }

    private void toggleTheme(Button button) {
        // Obtener el modo actual desde SharedPreferences
        SharedPreferences preferences = getSharedPreferences("settings", MODE_PRIVATE);
        SharedPreferences.Editor editor = preferences.edit();

        //Cambiar al modo noche automaticamente
        if (AppCompatDelegate.getDefaultNightMode() == AppCompatDelegate.MODE_NIGHT_NO) {
            AppCompatDelegate.setDefaultNightMode(AppCompatDelegate.MODE_NIGHT_YES);
            editor.putBoolean("dark_mode", true);
        } else {
            AppCompatDelegate.setDefaultNightMode(AppCompatDelegate.MODE_NIGHT_NO);
            editor.putBoolean("dark_mode", false);
        }
        editor.apply();
    }
    private void updateThemeButtonText(boolean isDarkMode) {
        // Cambiar el texto del botón según el modo
        if (isDarkMode) {
            themeButton.setText("Modo Claro");
        } else {
            themeButton.setText("Modo Oscuro");
        }
    }
}