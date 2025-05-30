using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.UI;
using UnityEngine.SceneManagement;

public class PlayerHealth : MonoBehaviour
{
    public bool isDead { get; private set; }
    public static PlayerHealth Instance;

    [SerializeField] private int maxHealth = 3;
    [SerializeField] private float knockBackThrustAmount = 10f;
    [SerializeField] private float damageRecoveryTime = 1f;
    [SerializeField] private AudioClip damageSFX;

    private Slider healthSlider;
    private int currentHealth;
    private bool canTakeDamage = true;
    private Knockback knockback;
    private Flash flash;
    private AudioSource audioSource;

    const string HEALTH_SLIDER_TEXT = "Health Slider";
    const string TOWN_TEXT = "Level1";
    readonly int DEATH_HASH = Animator.StringToHash("Death");

    private void Awake() {
        Instance = this;
        flash = GetComponent<Flash>();
        knockback = GetComponent<Knockback>();
        audioSource = GetComponent<AudioSource>();
    }

    private void Start() {
        isDead = false;
        currentHealth = maxHealth;

        UpdateHealthSlider();
    }

    private void OnTriggerEnter2D(Collider2D other)
    {
        SpikeTrap trap = other.GetComponent<SpikeTrap>();
        EnemyAI enemy = other.GetComponentInParent<EnemyAI>();

        if (trap && canTakeDamage) {
            TakeDamage(1, other.transform);
            knockback.GetKnockedBack(other.transform, knockBackThrustAmount);
            StartCoroutine(flash.FlashRoutine());
        }
        else if (enemy && canTakeDamage) {
            TakeDamage(1, other.transform);
            knockback.GetKnockedBack(other.transform, knockBackThrustAmount);
            StartCoroutine(flash.FlashRoutine());
        }
    }


    private void HealPlayer() {
        if (currentHealth < maxHealth) {
            currentHealth += 1;
            UpdateHealthSlider();
        }
    }

    private void TakeDamage(int damageAmount, Transform hitTransform) {
        knockback.GetKnockedBack(hitTransform, knockBackThrustAmount);
        canTakeDamage = false;
        currentHealth -= damageAmount;
        StartCoroutine(DamageRecoveryRoutine());
        UpdateHealthSlider();
        CheckIfPlayerIsDeath();
        if (damageSFX != null && audioSource != null)
            audioSource.PlayOneShot(damageSFX);

    }

    private void CheckIfPlayerIsDeath()
    {
        if (currentHealth <= 0 && !isDead)
        {
            isDead = true;
            currentHealth = 0;
            GetComponent<Animator>().SetTrigger(DEATH_HASH);

            if (CheckpointManager.Instance.lastCheckpointPosition != null)
            {
                // Respawn dengan delay agar animasi sempat dimainkan
                StartCoroutine(RespawnRoutine());
            }
            else
            {
                StartCoroutine(DeathLoadSceneRoutine());
            }
        }
    }

    private IEnumerator RespawnRoutine()
    {
        yield return new WaitForSeconds(3f); // Tunggu 1 detik agar animasi mati dimainkan

        // Reset posisi player
        transform.position = (Vector2)CheckpointManager.Instance.lastCheckpointPosition;

        // Reset state
        currentHealth = maxHealth;
        isDead = false;
        UpdateHealthSlider();

        // Reset animator
        Animator anim = GetComponent<Animator>();
        anim.ResetTrigger(DEATH_HASH); // opsional
        anim.Play("Idle"); // ganti dengan nama animasi idle default kamu

        Debug.Log("Respawn ke checkpoint.");
    }

    private IEnumerator DeathLoadSceneRoutine()
    {
        yield return new WaitForSeconds(2f);
        Destroy(gameObject);
        UnityEngine.SceneManagement.SceneManager.LoadScene(TOWN_TEXT);
    }

    private IEnumerator DamageRecoveryRoutine() {
        yield return new WaitForSeconds(damageRecoveryTime);
        canTakeDamage = true;
    }

    private void UpdateHealthSlider() {
        if (healthSlider == null) {
            healthSlider = GameObject.Find("Health Slider").GetComponent<Slider>();
        }

        healthSlider.maxValue = maxHealth;
        healthSlider.value = currentHealth;
    }
}
