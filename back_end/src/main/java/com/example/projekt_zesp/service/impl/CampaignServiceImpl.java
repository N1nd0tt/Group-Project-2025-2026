package com.example.projekt_zesp.service.impl;

import com.example.projekt_zesp.models.Campaign;
import com.example.projekt_zesp.models.User;
import com.example.projekt_zesp.repository.CampaignRepository;
import com.example.projekt_zesp.service.CampaignService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import java.util.List;
import java.util.Optional;

@Service
public class CampaignServiceImpl implements CampaignService {
    @Autowired
    private CampaignRepository campaignRepository;

    @Autowired
    private com.example.projekt_zesp.repository.ChatMessageRepository chatMessageRepository;

    @Override
    public Campaign addPlayerToCampaign(String campaignId, User player) {
        Optional<Campaign> optionalCampaign = campaignRepository.findById(campaignId);
        if (optionalCampaign.isPresent()) {
            Campaign campaign = optionalCampaign.get();
            campaign.getPlayers().add(player);
            return campaignRepository.save(campaign);
        }
        throw new RuntimeException("Campaign not found");
    }

    @Override
    public Campaign removePlayerFromCampaign(String campaignId, String playerId) {
        Optional<Campaign> optionalCampaign = campaignRepository.findById(campaignId);
        if (optionalCampaign.isPresent()) {
            Campaign campaign = optionalCampaign.get();
            campaign.getPlayers().removeIf(p -> p.getId().equals(playerId));
            return campaignRepository.save(campaign);
        }
        throw new RuntimeException("Campaign not found");
    }

    @Override
    public Campaign getCampaignInfo(String campaignId) {
        return campaignRepository.findById(campaignId)
                .orElseThrow(() -> new RuntimeException("Campaign not found"));
    }

    @Override
    public List<Campaign> getAllCampaignsByOwner(String ownerId) {
        return campaignRepository.findAll().stream()
                .filter(campaign -> campaign.getOwnerId().equals(ownerId))
                .toList();
    }

    @Override
    public List<com.example.projekt_zesp.models.ChatMessage> getCampaignChat(String campaignId) {
        return chatMessageRepository.findByCampaignIdOrderByCreatedAtAsc(campaignId);
    }
}
