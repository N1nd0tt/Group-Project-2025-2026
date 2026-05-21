package com.example.projekt_zesp.service.impl;

import com.example.projekt_zesp.dto.UserProfileDto;
import com.example.projekt_zesp.models.Campaign;
import com.example.projekt_zesp.models.History;
import com.example.projekt_zesp.models.User;
import com.example.projekt_zesp.repository.CampaignRepository;
import com.example.projekt_zesp.repository.HistoryRepository;
import com.example.projekt_zesp.repository.UserRepository;
import com.example.projekt_zesp.service.UserService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import java.util.List;

@Service
public class UserServiceImpl implements UserService {

    @Autowired
    private UserRepository userRepository;

    @Autowired
    private CampaignRepository campaignRepository;

    @Autowired
    private HistoryRepository historyRepository;

    @Override
    public UserProfileDto getUserProfile(String userId) {
        User user = userRepository.findById(userId)
                .orElseThrow(() -> new RuntimeException("User not found"));

        List<Campaign> ownedCampaigns = campaignRepository.findByOwnerId(userId);
        List<Campaign> playingCampaigns = campaignRepository.findByPlayersId(userId);
        List<History> history = historyRepository.findByOwnerId(userId);

        return UserProfileDto.builder()
                .id(user.getId())
                .login(user.getLogin())
                .ownedCampaigns(ownedCampaigns)
                .playingCampaigns(playingCampaigns)
                .history(history)
                .build();
    }
}
