package com.example.warframes.views;

import android.content.Context;
import android.content.Intent;
import android.content.SharedPreferences;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;

import androidx.appcompat.app.AppCompatActivity;
import androidx.appcompat.app.AppCompatDelegate;
import androidx.databinding.DataBindingUtil;
import androidx.lifecycle.ViewModelProvider;
import androidx.recyclerview.widget.LinearLayoutManager;

import com.example.warframes.R;
import com.example.warframes.adapters.WarframeAdapter;
import com.example.warframes.databinding.ActivityFavoritesBinding;
import com.example.warframes.viewmodels.FavoriteViewModel;

import java.util.ArrayList;

public class FavoritesActivity extends AppCompatActivity {
    private FavoriteViewModel viewModel;
    private WarframeAdapter adapter;
    private Context context = this;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        ActivityFavoritesBinding binding = DataBindingUtil.setContentView(this, R.layout.activity_favorites);
        SharedPreferences preferences = getSharedPreferences("settings", MODE_PRIVATE);
        boolean isDarkMode = preferences.getBoolean("dark_mode", false);

        // Aplicar el tema según la preferencia
        if (isDarkMode) {
            AppCompatDelegate.setDefaultNightMode(AppCompatDelegate.MODE_NIGHT_YES);
        } else {
            AppCompatDelegate.setDefaultNightMode(AppCompatDelegate.MODE_NIGHT_NO);
        }

        Button backButton = findViewById(R.id.backButton);
        //Adapter con un listener clics
        adapter = new WarframeAdapter(new ArrayList<>(), warframe -> {
            //Intent a DetailActivity
            Intent intent = new Intent(this, DetailActivity.class);
            intent.putExtra("id", warframe.getId());
            intent.putExtra("name", warframe.getName());
            intent.putExtra("description", warframe.getDescription());
            intent.putExtra("url", warframe.getUrl());
            startActivity(intent);
        });

        //Configurar el RecyclerView
        binding.recyclerViewFavorites.setLayoutManager(new LinearLayoutManager(this));
        binding.recyclerViewFavorites.setAdapter(adapter);

        // Configura el ViewModel
        viewModel = new ViewModelProvider(this).get(FavoriteViewModel.class);
        viewModel.getFavoriteWarframes().observe(this, warframes -> adapter.setWarframe(warframes));
        backButton.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                Intent myIntent = new Intent(context, DashboardActivity.class);
                context.startActivity(myIntent);
            }
        });
    }
}
