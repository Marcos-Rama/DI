package com.example.warframes.adapters;

import android.view.LayoutInflater;
import android.view.ViewGroup;
import androidx.annotation.NonNull;
import androidx.databinding.DataBindingUtil;
import androidx.recyclerview.widget.RecyclerView;

import com.example.warframes.R;
import com.example.warframes.databinding.ItemProductBinding;
import com.example.warframes.models.Warframe;

import java.util.List;


public class WarframeAdapter extends RecyclerView.Adapter<WarframeAdapter.WarframeViewHolder> {
    private List<Warframe> warframes;

    public WarframeAdapter(List<Warframe> warframes) {
        this.warframes = warframes;
    }

    public void setWarframe(List<Warframe> warframes) {
        this.warframes = warframes;
        notifyDataSetChanged();
    }

    @NonNull
    @Override
    public WarframeViewHolder onCreateViewHolder(@NonNull ViewGroup parent, int viewType) {
        ItemProductBinding binding = DataBindingUtil.inflate(
                LayoutInflater.from(parent.getContext()),
                R.layout.item_product,
                parent,
                false
        );
        return new WarframeViewHolder(binding);
    }

    @Override
    public void onBindViewHolder(@NonNull WarframeViewHolder holder, int position) {
        Warframe warframe = warframes.get(position);
        holder.bind(warframe);
    }

    @Override
    public int getItemCount() {
        return warframes != null ? warframes.size() : 0;
    }

    static class WarframeViewHolder extends RecyclerView.ViewHolder {
        private final ItemProductBinding binding;

        public WarframeViewHolder(@NonNull ItemProductBinding binding) {
            super(binding.getRoot());
            this.binding = binding;
        }

        public void bind(Warframe warframe) {
            binding.setWarframe(warframe);
            binding.executePendingBindings();
        }
    }
}