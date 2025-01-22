package com.example.warframes.repositories;

import androidx.lifecycle.MutableLiveData;

import com.example.warframes.models.Warframe;
import com.google.firebase.database.DataSnapshot;
import com.google.firebase.database.DatabaseError;
import com.google.firebase.database.DatabaseReference;
import com.google.firebase.database.FirebaseDatabase;
import com.google.firebase.database.ValueEventListener;

import java.util.ArrayList;
import java.util.List;

public class DashboardRepository {
    private final DatabaseReference warframeRef;

    public DashboardRepository() {
        warframeRef = FirebaseDatabase.getInstance().getReference("warframes");
    }

    public void getWarframes(MutableLiveData<List<Warframe>> warframeLiveData) {
        warframeRef.addValueEventListener(new ValueEventListener() {
            @Override
            public void onDataChange(DataSnapshot snapshot) {
                List<Warframe> warframes = new ArrayList<>();
                for (DataSnapshot child : snapshot.getChildren()) {
                    Warframe warframe = child.getValue(Warframe.class);
                    warframes.add(warframe);
                }
                warframeLiveData.setValue(warframes);
            }

            @Override
            public void onCancelled(DatabaseError error) {
                // Manejo de errores
            }
        });
    }

}
