using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public partial class PlayerController : Singleton<PlayerController>
{
    [SerializeField] private float moveSpeed = 1f;

    private PlayerControls playerControls;
    private Vector2 movement;
    private Rigidbody2D rb;
    private Animator myAnimator;
    private SpriteRenderer mySpriteRender;
    private Knockback knockback;


    protected override void Awake()
    {
        base.Awake();
        
        playerControls = new PlayerControls();
        rb = GetComponent<Rigidbody2D>();
        myAnimator = GetComponent<Animator>();
        mySpriteRender = GetComponent<SpriteRenderer>();
        knockback = GetComponent<Knockback>();

        if (PlayerController.Instance != this)
        {
            Destroy(gameObject); // cegah duplikat
            return;
        }

        DontDestroyOnLoad(gameObject);
    }

    private void OnEnable()
    {
        playerControls.Enable();
    }

    private void OnDisable()
    {
        playerControls.Disable();
    }

    private void Update()
    {
        PlayerInput();
        AdjustPlayerFacingDirection();
    }

    private void FixedUpdate()
    {
        Move();
    }

    private void PlayerInput()
    {
        movement = playerControls.Movement.Move.ReadValue<Vector2>();

        myAnimator.SetFloat("moveX", movement.x);
        myAnimator.SetFloat("moveY", movement.y);
    }

    private void Move()
    {
        if (knockback == null || PlayerHealth.Instance == null) return;

        if (knockback.GettingKnockedBack || PlayerHealth.Instance.isDead)
            return;

        rb.MovePosition(rb.position + movement * (moveSpeed * Time.fixedDeltaTime));
    }

    private void AdjustPlayerFacingDirection()
    {
        if (movement.x < 0)
        {
            mySpriteRender.flipX = true;  // Menghadap kiri
        }
        else if (movement.x > 0)
        {
            mySpriteRender.flipX = false; // Menghadap kanan
        }
    }

}
