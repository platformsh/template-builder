<?php
// api/src/Entity/Product.php
namespace App\Entity;

use ApiPlatform\Metadata\ApiResource;
use Doctrine\ORM\Mapping as ORM;
use Doctrine\Common\Collections\ArrayCollection;
use Symfony\Component\Validator\Constraints as Assert;

#[ORM\Entity]
#[ApiResource]
class Product // The class name will be used to name exposed resources
{
    #[ORM\Id, ORM\Column, ORM\GeneratedValue]
    private ?int $id = null;

    /**
     * A name property - this description will be available in the API documentation too.
     *
     */
    #[ORM\Column]
    #[Assert\NotBlank]
    public string $name = '';

    // Notice the "cascade" option below, this is mandatory if you want Doctrine to automatically persist the related entity
    /**
     * @var Offer[]|ArrayCollection
     *
     */
    #[ORM\OneToMany(targetEntity: Offer::class, mappedBy: 'product', cascade: ['persist'])]
    public iterable $offers;

    public function __construct()
    {
        $this->offers = new ArrayCollection(); // Initialize $offers as a Doctrine collection
    }

    public function getId(): ?int
    {
        return $this->id;
    }

    // Adding both an adder and a remover as well as updating the reverse relation is mandatory
    // if you want Doctrine to automatically update and persist (thanks to the "cascade" option) the related entity
    public function addOffer(Offer $offer): void
    {
        $offer->product = $this;
        $this->offers->add($offer);
    }

    public function removeOffer(Offer $offer): void
    {
        $offer->product = null;
        $this->offers->removeElement($offer);
    }

    // ...
}