package com.example.projekt_zesp.dto;

import com.example.projekt_zesp.models.Campaign;
import com.example.projekt_zesp.models.History;
import com.example.projekt_zesp.models.User;
import lombok.AllArgsConstructor;
import lombok.Builder;
import lombok.Data;
import lombok.NoArgsConstructor;

import java.util.List;

@Data
@Builder
@NoArgsConstructor
@AllArgsConstructor
public class UserProfileDto {
    private String id;
    private String login;
    private List<Campaign> ownedCampaigns;
    private List<Campaign> playingCampaigns;
    private List<History> history;
}
