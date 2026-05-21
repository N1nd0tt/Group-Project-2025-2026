package com.example.projekt_zesp.controller;

import com.example.projekt_zesp.models.Campaign;
import com.example.projekt_zesp.models.User;
import com.example.projekt_zesp.service.CampaignService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;

import java.util.List;

@RestController
@RequestMapping("/campaigns")
public class CampaignController {

    @Autowired
    private CampaignService campaignService;

    @PostMapping("/{campaignId}/players")
    public ResponseEntity<Campaign> addPlayerToCampaign(@PathVariable String campaignId, @RequestBody User player) {
        Campaign updatedCampaign = campaignService.addPlayerToCampaign(campaignId, player);
        return ResponseEntity.ok(updatedCampaign);
    }

    @DeleteMapping("/{campaignId}/players/{playerId}")
    public ResponseEntity<Campaign> removePlayerFromCampaign(@PathVariable String campaignId, @PathVariable String playerId) {
        Campaign updatedCampaign = campaignService.removePlayerFromCampaign(campaignId, playerId);
        return ResponseEntity.ok(updatedCampaign);
    }

    @GetMapping("/{campaignId}")
    public ResponseEntity<Campaign> getCampaignInfo(@PathVariable String campaignId) {
        Campaign campaign = campaignService.getCampaignInfo(campaignId);
        return ResponseEntity.ok(campaign);
    }

    @GetMapping("/owner/{ownerId}")
    public ResponseEntity<List<Campaign>> getAllCampaignsByOwner(@PathVariable String ownerId) {
        List<Campaign> campaigns = campaignService.getAllCampaignsByOwner(ownerId);
        return ResponseEntity.ok(campaigns);
    }

    @GetMapping("/{campaignId}/chat")
    public ResponseEntity<List<com.example.projekt_zesp.models.ChatMessage>> getCampaignChat(@PathVariable String campaignId) {
        return ResponseEntity.ok(campaignService.getCampaignChat(campaignId));
    }
}
