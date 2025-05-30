using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class Checkpoint : MonoBehaviour
{
    private Animator animator;
    private bool isActivated = false;

    private void Awake()
    {
        animator = GetComponent<Animator>();
    }

    private void OnTriggerEnter2D(Collider2D collision)
    {
        if (!isActivated && collision.CompareTag("Player") && CheckpointManager.Instance != null)
        {
            isActivated = true;

            // Simpan checkpoint
            CheckpointManager.Instance.SetCheckpoint(transform.position);

            // Aktifkan animasi
            if (animator != null)
            {
                animator.SetBool("isActive", true);
            }
        }
    }
}

