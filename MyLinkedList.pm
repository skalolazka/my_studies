package MyLinkedList;

use strict;
use warnings;

sub new {
    my ($class, @values) = @_;
    my $self = { first => undef, last => undef};
    my $prev = undef;
    for (my $i = 0; $i < scalar(@values); $i++) {
        my %cur = ( value => $values[$i], next_node => undef );
        if ($i == 0) {
            $prev = \%cur;
            $self->{first} = $prev;
        }
        else {
            $prev->{next_node} = \%cur;
        }
        $prev = \%cur;
    }
    $self->{last} = $prev;
    return bless $self => $class;
}

1;
