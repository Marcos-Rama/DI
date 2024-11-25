package com.example.mycatalog;

import android.os.Bundle;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.ImageView;

import androidx.annotation.NonNull;
import androidx.annotation.Nullable;
import androidx.fragment.app.Fragment;

import com.squareup.picasso.Picasso;

public class DetailFragment extends Fragment {

    //"Infla" el fragment que se mostrará según lo establecido en el xml detail_fragment
    @Nullable
    @Override
    public View onCreateView(@NonNull LayoutInflater inflater, @Nullable ViewGroup container, @Nullable Bundle savedInstanceState) {
        View view = inflater.inflate(R.layout.detail_fragment, container, false);
        // Load image using Picasso
        ImageView imageView = view.findViewById(R.id.Imagen1);
        Picasso.get().load(R.drawable.carta5)
                .transform(new CircleTransform())
                .into(imageView);

        return view;
    }
}