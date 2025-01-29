package com.example.warframes.views;

import android.content.Intent;
import android.os.Bundle;
import android.util.Log;
import android.view.View;
import android.widget.Button;
import android.content.Context;

import androidx.appcompat.app.AppCompatActivity;
import androidx.databinding.DataBindingUtil;
import androidx.lifecycle.ViewModelProvider;
import androidx.recyclerview.widget.LinearLayoutManager;

import com.example.warframes.R;
import com.example.warframes.adapters.WarframeAdapter;
import com.example.warframes.databinding.ActivityDashboardBinding;
import com.example.warframes.viewmodels.DashboardViewModel;

import java.util.ArrayList;

public class DashboardActivity extends AppCompatActivity {
    //ViewModel para los datos de warframes
    private DashboardViewModel warframeViewModel;
    //Adapter para el recycler
    private WarframeAdapter warframeAdapter;
    private Context context = this;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        //Configura el binding para la vista del dashboard
        ActivityDashboardBinding binding = DataBindingUtil.setContentView(this, R.layout.activity_dashboard);


        Button logOutButton = findViewById(R.id.logOutButtonMain);

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
}