package MyLinkedList;

use strict;
use warnings;

sub from_array {
    my ($class, @values) = @_;
    return undef unless scalar(@values);
    my $self = {};
    my $prev = undef;
    for (my $i = 0; $i < scalar(@values); $i++) {
        my %cur = ( value => $values[$i], next_node => undef );
        if ($i == 0) {
            $prev = \%cur;
            $self = $prev;
        }
        else {
            $prev->{next_node} = \%cur;
        }
        $prev = \%cur;
    }
    return bless $self => $class;
}

sub to_array {
    my $self = shift;
    my @arr = ();
    my $ptr = $self;
    while (defined($ptr)) {
        push(@arr, $ptr->{value});
        $ptr = $ptr->{next_node};
    }
    return @arr;
}

1;
