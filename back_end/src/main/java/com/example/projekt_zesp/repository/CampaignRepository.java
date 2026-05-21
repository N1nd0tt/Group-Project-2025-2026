package com.example.projekt_zesp.repository;

import com.example.projekt_zesp.models.Campaign;
import org.springframework.data.jpa.repository.JpaRepository;
import java.util.List;

public interface CampaignRepository extends JpaRepository<Campaign, String> {
    List<Campaign> findByOwnerId(String ownerId);
    List<Campaign> findByPlayersId(String playerId);
}
