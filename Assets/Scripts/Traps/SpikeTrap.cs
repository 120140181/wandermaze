using System.Collections;
using UnityEngine;

public class SpikeTrap : MonoBehaviour
{
    [SerializeField] private float animationDuration = 0.5f;

    private Animator animator;
    private bool isWorking = false;

    private void Awake() {
        animator = GetComponent<Animator>();
    }

    private void OnTriggerEnter2D(Collider2D other) {
        if (other.CompareTag("Player") && !isWorking) {
            StartCoroutine(TriggerTrap());
        }
    }

    private IEnumerator TriggerTrap() {
        isWorking = true;
        animator.SetTrigger("isWorking");

        // Tunggu animasi selesai
        yield return new WaitForSeconds(animationDuration);

        animator.ResetTrigger("isWorking");
        isWorking = false;
    }

    public bool IsWorking() {
        return isWorking;
    }
}

