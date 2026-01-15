package com.example.projekt_zesp.service;

import com.example.projekt_zesp.models.Invitation;

import java.util.List;

public interface InvitationService {
    Invitation sendInvitation(Invitation invitation);
    List<Invitation> getReceivedInvitations(String receiverId);
    List<Invitation> getSentInvitations(String senderId);
    void updateInvitationStatus(Long id, String status);
}
