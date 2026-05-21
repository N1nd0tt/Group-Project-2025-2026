package com.example.projekt_zesp.controller;

import com.example.projekt_zesp.models.Invitation;
import com.example.projekt_zesp.service.InvitationService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;

import java.util.List;

@RestController
@RequestMapping("/invitations")
public class InvitationController {

    @Autowired
    private InvitationService invitationService;

    @PostMapping
    public ResponseEntity<Invitation> sendInvitation(@RequestBody Invitation invitation) {
        return ResponseEntity.ok(invitationService.sendInvitation(invitation));
    }

    @GetMapping("/received/{receiverId}")
    public ResponseEntity<List<Invitation>> getReceivedInvitations(@PathVariable String receiverId) {
        return ResponseEntity.ok(invitationService.getReceivedInvitations(receiverId));
    }

    @GetMapping("/sent/{senderId}")
    public ResponseEntity<List<Invitation>> getSentInvitations(@PathVariable String senderId) {
        return ResponseEntity.ok(invitationService.getSentInvitations(senderId));
    }

    @PutMapping("/{id}/status")
    public ResponseEntity<Void> updateInvitationStatus(@PathVariable Long id, @RequestParam String status) {
        invitationService.updateInvitationStatus(id, status);
        return ResponseEntity.noContent().build();
    }
}
