package com.example.projekt_zesp.service.impl;

import com.example.projekt_zesp.models.Invitation;
import com.example.projekt_zesp.repository.InvitationRepository;
import com.example.projekt_zesp.service.InvitationService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import java.util.List;

@Service
public class InvitationServiceImpl implements InvitationService {
    @Autowired
    private InvitationRepository invitationRepository;

    @Override
    public Invitation sendInvitation(Invitation invitation) {
        return invitationRepository.save(invitation);
    }

    @Override
    public List<Invitation> getReceivedInvitations(String receiverId) {
        return invitationRepository.findByReceiverId(receiverId);
    }

    @Override
    public List<Invitation> getSentInvitations(String senderId) {
        return invitationRepository.findBySenderId(senderId);
    }

    @Override
    public void updateInvitationStatus(Long id, String status) {
        Invitation invitation = invitationRepository.findById(id)
                .orElseThrow(() -> new RuntimeException("Invitation not found"));
        invitation.setStatus(status);
        invitationRepository.save(invitation);
    }
}
