package com.example.projekt_zesp.service;

import com.example.projekt_zesp.models.Campaign;
import com.example.projekt_zesp.models.User;

import java.util.List;

public interface CampaignService {
    Campaign addPlayerToCampaign(String campaignId, User player);
    Campaign removePlayerFromCampaign(String campaignId, String playerId);
    Campaign getCampaignInfo(String campaignId);
    List<Campaign> getAllCampaignsByOwner(String ownerId);
    List<com.example.projekt_zesp.models.ChatMessage> getCampaignChat(String campaignId);
}
