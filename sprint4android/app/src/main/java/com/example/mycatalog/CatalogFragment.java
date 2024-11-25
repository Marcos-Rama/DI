package com.example.mycatalog;

import android.os.Bundle;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.Button;

import androidx.annotation.NonNull;
import androidx.annotation.Nullable;
import androidx.fragment.app.Fragment;

public class CatalogFragment extends Fragment {

    public CatalogFragment() {
    }

    //"Infla" el fragment que se mostrará según lo establecido en el xml catalog_fragment
    @Nullable
    @Override
    public View onCreateView(@NonNull LayoutInflater inflater, @Nullable ViewGroup container, @Nullable Bundle savedInstanceState) {
        View view = inflater.inflate(R.layout.catalog_fragment, container, false);
        // Botón que redicciona a la siguiente pantalla que en este caso será la que muestra la información de detail
        Button button = view.findViewById(R.id.Button1);
        button.setOnClickListener(v -> {
            getParentFragmentManager()
                    .beginTransaction()
                    .replace(R.id.fragmentContainer, new DetailFragment())
                    .addToBackStack(null)
                    .commit();
        });

        return view;
    }

}
