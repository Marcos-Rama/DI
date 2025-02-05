package com.example.warframes.views;

import android.content.Intent;
import android.os.Bundle;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;

import androidx.databinding.DataBindingUtil;
import androidx.fragment.app.Fragment;
import androidx.lifecycle.ViewModelProvider;
import androidx.recyclerview.widget.LinearLayoutManager;

import com.example.warframes.R;
import com.example.warframes.adapters.WarframeAdapter;
import com.example.warframes.databinding.FavoritesFragmentBinding;
import com.example.warframes.viewmodels.FavoriteViewModel;

import java.util.ArrayList;

public class FavoritesFragment extends Fragment {
    private FavoriteViewModel viewModel;
    private WarframeAdapter adapter;

    public FavoritesFragment() {
        // Constructor vacío requerido
    }

    @Override
    public View onCreateView(LayoutInflater inflater, ViewGroup container, Bundle savedInstanceState) {
        View view = inflater.inflate(R.layout.favorites_fragment, container, false);
        FavoritesFragmentBinding binding = DataBindingUtil.bind(view);

        if (binding == null) {
            throw new IllegalStateException("Error al inflar fragment_favorites");
        }

        // Configurar el Adapter con listener para clics
        adapter = new WarframeAdapter(new ArrayList<>(), warframe -> {
            Intent intent = new Intent(requireContext(), DetailActivity.class);
            intent.putExtra("id", warframe.getId());
            intent.putExtra("name", warframe.getName());
            intent.putExtra("description", warframe.getDescription());
            intent.putExtra("url", warframe.getUrl());
            startActivity(intent);
        });

        // Configurar RecyclerView
        binding.recyclerViewFavorites.setLayoutManager(new LinearLayoutManager(requireContext()));
        binding.recyclerViewFavorites.setAdapter(adapter);

        // Configurar ViewModel
        viewModel = new ViewModelProvider(this).get(FavoriteViewModel.class);
        viewModel.getFavoriteWarframes().observe(getViewLifecycleOwner(), warframes -> adapter.setWarframe(warframes));


        return view;
    }
}

