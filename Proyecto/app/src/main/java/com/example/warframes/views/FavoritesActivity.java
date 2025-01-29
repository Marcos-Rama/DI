package com.example.warframes.views;

import android.content.Intent;
import android.os.Bundle;

import androidx.appcompat.app.AppCompatActivity;
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

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        ActivityFavoritesBinding binding = DataBindingUtil.setContentView(this, R.layout.activity_favorites);

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
    }
}
